from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def root():
    return "This is the root page of the web-app"


#EXAMPLE OF URL PARAMS
@app.route("/hello")
def hello():
    name = request.args.get('name', '')
    if name == '':
        return "no param supplied"
    else:
        return "Hello %s" % name