from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/')
def root():
    return "This is the root page of the web-app"

#Upload an img file and save it to the static sub directory,
@app.route("/upload/", methods=['POST', 'GET'])
def upload():
    #Once uploaded, display img
    if request.method == 'POST':
        file = request.files['datafile']
        file.save('static/uploads/file.png')
        return '<img src="'+url_for('static', filename='uploads/file.png')+'"/>'
    else:
        page ='''
        <html>
            <body>
                <form action="" method="post" name="form" enctype="multipart/form-data">
                    <input type="file" name="datafile" />
                    <input type="submit" name="submit" id="submit" />
                </form>
            </body>
        </html>
        '''
        return page, 200
    

