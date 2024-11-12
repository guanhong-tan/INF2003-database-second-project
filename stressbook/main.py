from flask import Flask, render_template, request, url_for, redirect , flash , session , abort
from datetime import datetime
from models import user , event , seat

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a strong secret key
# Pass the db instance to the models

@app.route('/')
def index():
    events = list(event.retrieve_events())
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
        user_data = user.user_login(email,password)  
        if user_data:
            # If login is successful, set session variables
            session['logged_in'] = True
            session['user_id'] = str(user_data['_id'])  # Store user ID in session
            session['user_email'] = user_data['email']  # Store user email for display
            session['name'] = user_data['name'] # Store user ID in session
            flash("Logged in successfully.", "success")
            return redirect(url_for('events'))  
        else:
            flash("Invalid email or password.", "danger")  

    return render_template("login.html")


@app.route("/events")
def events():
    events = list(event.retrieve_events())
    return render_template("events.html",events=events)

@app.route("/event/<event_id>")
def event_detail(event_id):
    event_detail = event.get_event_by_id(event_id)
    if event_detail:
        # current_url = request.url
        current_path = request.path
        return render_template("event_details.html", event=event_detail , current_path=current_path)
    else:
        abort(404)  # If event not found, return a 404 error

@app.route("/event/<event_id>/seating")
def booking_concert_seat(event_id):
    event_data = event.get_event_by_id(event_id)
    # seats = seat.get_seats_by_event(event_id)  # Retrieve seats for the event
    if event_data:
        # return render_template("booking_concert_seat.html", event=event_data, seats=seats)
        return render_template("booking_concert_seat.html", event=event_data)
    else:
        abort(404)  # Return a 404 error if the event is not found

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
def dashboard():
    return render_template("dashboard.html")

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
    
if __name__ == "__main__":
    event.create_events_onload()
    app.run(debug=True,threaded=True)