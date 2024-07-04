from flask import *
from PIL import Image
from io import BytesIO


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Error 403 - Forbidden</h1><hr>You don\'t have permission to access this resource', 403


@app.route('/api/get-img' , methods=['GET','POST'])
def convert():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            image = Image.open(file.stream)
            image = image.convert('RGB')
            img_io = BytesIO()
            image.save(img_io , "JPEG")
            img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='img.jpg')

    return '<h1>Error 403 - Forbidden</h1><hr>You don\'t have permission to access this resource', 403


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Error 404 - Not Found</h1><hr>The resource could not be found.', 404
@app.errorhandler(500)
def internal_server_error(e):
    return '<h1>Error 500 - Internal Server Error</h1><hr>An internal server error occurred.', 500


app.run()