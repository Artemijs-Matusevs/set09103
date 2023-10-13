from flask import Flask, render_template
app = Flask(__name__)


#Simple example of rendering a Jinja2 template
@app.route('/hello/<name>')
def hello(name=None):
    user = {'name': name}
    return render_template('hello.html', user=user)


#Rendering a Jinja2 template containing a conditional clause
@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name=None):
    return render_template('conditional.html', name=name)