from flask import *
from PIL import Image
from io import BytesIO
from rembg import remove


app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Error 403 - Forbidden</h1><hr>You don\'t have permission to access this resource', 403


@app.route('/api/get-jpg' , methods=['GET','POST'])
def convert_jpg():
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
        return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='imgtools.jpg')

    return '<h1>Error 403 - Forbidden</h1><hr>You don\'t have permission to access this resource', 403

@app.route('/api/get-png' , methods=['GET','POST'])
def convert_png():
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
            image.save(img_io , "PNG")
            img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='imgtools.png')

    return '<h1>Error 403 - Forbidden</h1><hr>You don\'t have permission to access this resource', 403

@app.route('/api/get-webp' , methods=['GET','POST'])
def convert_webp():
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
            image.save(img_io , "WEBP")
            img_io.seek(0)
        return send_file(img_io, mimetype='image/webp', as_attachment=True, download_name='imgtools.webp')

    return '<h1>Error 403 - Forbidden</h1><hr>You don\'t have permission to access this resource', 403


@app.route('/api/rmbg', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        if file:
            input = Image.open(file.stream)
            output = remove(input, post_process_mask=True)
            img_io = BytesIO()
            output.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='imgtools_rm.png')
        
    return '<h1>Error 403 - Forbidden</h1><hr>You don\'t have permission to access this resource', 403


@app.errorhandler(404)
def page_not_found(e):
    return '<h1>Error 404 - Not Found</h1><hr>The resource could not be found.', 404
@app.errorhandler(500)
def internal_server_error(e):
    return '<h1>Error 500 - Internal Server Error</h1><hr>An internal server error occurred.', 500


if __name__ == "__main__":
    app.run()