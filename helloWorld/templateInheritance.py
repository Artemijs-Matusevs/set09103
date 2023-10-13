from flask import Flask, render_template
app = Flask(__name__)

#Display base template as the root
@app.route('/')
def root():
    return render_template('baseTemplate.html')


@app.route('/one/')
def inherits_one():
    return render_template('2ndTemplate.html')

@app.route('/two/')
def inherits_two():
    return render_template("3rdTemplate.html")