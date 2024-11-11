from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/register")
def register_account():
    return render_template("register.html")

@app.route("/login")
def login_account():
    return render_template("login.html")

@app.route("/concerts")
def concerts():
    return render_template("concerts.html")

@app.route("/threaters")
def threaters():
    return render_template("threaters.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)