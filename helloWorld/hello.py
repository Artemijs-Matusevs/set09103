from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return "This is the home route of my web-app"

#Generate a basic HTML with an img
@app.route('/static-example/img')
def static_example_img():
    url = url_for("static", filename="vmask.jpg")
    return '<img src="'+url+'">', 200


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


# Custom error message for error code 404
@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested. ", 300

