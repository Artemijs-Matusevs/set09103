from flask import Flask
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
