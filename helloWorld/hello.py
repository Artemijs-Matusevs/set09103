from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return "This is the home route of my web-app"


@app.route('/hello/')
def hello():
    return "Hello!"


@app.route('/goodbye/')
def goodbye():
    return "Goodbye!"

@app.route("/private")
def private():
    # Test for user log-in,
    # Redirect if failed,
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "LOGIN PAGE"