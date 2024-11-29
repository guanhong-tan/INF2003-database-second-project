from flask import Flask, render_template, request, url_for, redirect , flash , session , abort
from datetime import datetime
from models import user , event as event_model , seat
from utils import login_required  # Remove the dot for direct import

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key
# Pass the db instance to the models

@app.route('/')
def index():
    events = list(event_model.retrieve_events())
    return render_template('index.html',events=events)

@app.route("/register", methods=['GET', 'POST'])
def register_account():
    errors = { "name" : [] , "email" : [] , "password" : [] }
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Validate Name
        if not name:
            errors["name"].append("Email is required.")
        elif len(password) < 3:
            errors["name"].append("Name must be at least 3 characters long.")
        # Validate Email
        if not email:
            errors["email"].append("Email is required.")
        elif "@" not in email:
            errors["email"].append("Email must contain '@' symbol.")
        elif user.is_email_used(email):
            errors["email"].append("Email Address already exists. Choose a different one")

        # Validate Password 
        if not password:
            errors["password"].append("Password is required.")
        elif len(password) < 3:
            errors["password"].append("Password must be at least 3 characters long.")

        if not any(errors.values()):
            user.create_user(name,email,password)
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login_account'))
        
    return render_template("register.html",errors = errors)

@app.route("/login", methods=['GET', 'POST'])
def login_account():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists and if the password is correct
        user_data = user.user_login(email, password)  
        if user_data:
            # If login is successful, set session variables
            session['logged_in'] = True
            session['user_id'] = str(user_data['_id'])
            session['user_email'] = user_data['email']
            session['name'] = user_data['name']
            flash("Logged in successfully!", "success")
            return redirect(url_for('events'))
        else:
            flash("Invalid email or password. Please try again.", "danger")
            return render_template("login.html")

    return render_template("login.html")


@app.route("/events")
def events():
    events = list(event_model.retrieve_events())
    return render_template("events.html",events=events)

@app.route("/event/<event_id>")
def event_detail(event_id):
    event = event_model.get_event_by_id(event_id)
    if not event:
        abort(404)  # Raise 404 if event not found
    return render_template('event_details.html', event=event)

@app.route("/user_profile", methods=['GET', 'POST'])
def user_profile():
    return render_template("user_profile.html")

@app.route("/update_profile_details", methods=['GET', 'POST'])
def update_profile_details():
    if not session.get('logged_in'):
        flash("Please log in to access your profile.")
        return redirect(url_for('login_account'))
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Get updated data from the form
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        print(session['user_id'], name, email)
        user.update_user_profile(session['user_id'], name=name, email=email)
        flash("Profile updated successfully.", "success")
        return redirect(url_for('user_profile'))
    return render_template("user_profile.html")

@app.route("/dashboard")
@login_required
def dashboard():
    # You'll need to implement this function to get user's bookings
    # For now, we'll pass an empty list
    bookings = []  # Replace this with actual booking data when implemented
    return render_template('dashboard.html', bookings=bookings)

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('index'))  # Redirect to login page or homepage

# The @app.template_filter('datetimeformat') decorator in Flask is used to create a custom Jinja2 filter named datetimeformat, which you can use in your templates. This filter allows you to apply custom formatting to data directly within your Jinja2 templates.
@app.template_filter('datetimeformat')
def datetimeformat(value, format='%Y-%m-%d %H:%M'):
    try:
        date_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")  # Adjust format if necessary
        return date_obj.strftime(format)
    except (ValueError, TypeError):
        return value  # Return the original value if it can't be parsed
    
@app.route('/booking/confirm')
@login_required  # Add this decorator
def booking_confirm():
    event_id = request.args.get('event_id')
    event = event_model.get_event_by_id(event_id)
    return render_template('booking_confirm.html',
        event=event,
        section=request.args.get('section'),
        section_type=request.args.get('section_type'),
        price=request.args.get('price')
    )

@app.route('/booking/process', methods=['POST'])
def process_booking():
    event_id = request.form.get('event_id')
    section = request.form.get('section')
    price = request.form.get('price')
    quantity = request.form.get('quantity')

    # Get the event details
    event = event_model.get_event_by_id(event_id)

    # TODO: Add your booking logic here
    # For example:
    # - Check if tickets are still available
    # - Create booking record in database
    # - Update ticket count
    # - etc.

    # For now, just redirect to a success page or back to events
    flash('Booking successful!', 'success')
    return redirect(url_for('events'))

@app.route('/reset_db')
def reset_database():
    from models.event import reset_events
    reset_events()
    return "Database reset successfully"

@app.route('/booking/concert-seat/<event_id>')
@login_required
def booking_concert_seat(event_id):
    event = event_model.get_event_by_id(event_id)
    if not event:
        abort(404)
    return render_template('booking_concert_seat.html', event=event)

@app.route('/profile')
@login_required  # Add this decorator
def profile():
    return render_template('profile.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403

if __name__ == "__main__":
    event_model.reset_events()
    event_model.create_events_onload()
    seat.initialize_seat_sections()
    app.run(debug=True,threaded=True)