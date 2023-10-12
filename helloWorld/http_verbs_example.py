from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def root():
    return '''
    <html>
        <body>
            <a href="/account"> ACCOUNT </a>
        </body>
    </html>'''

@app.route("/account", methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        print (request.form)
        return "Hello %s" % request.form['name']
    else:
        page = '''
        <html>
            <body>
                <form action="" method="post" name="form">
                    <label for="name">Name:</label>
                    <input type="text" name="name" id="name"/>
                    <input type="submit" name="submit" id="submit"/>
                </form>
            </body>
        </html>'''

        return page