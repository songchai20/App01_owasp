import os
from flask import Flask, request, render_template_string, abort

app = Flask(__name__)

# กำหนดขนาดไฟล์สูงสุดเป็น 5 MB (5 * 1024 * 1024 ไบต์)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

#ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return '''
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')

    if file:
        if allowed_file(file.filename):
            # ตรวจสอบขนาดไฟล์
            file_path = os.path.join('uploads', file.filename)
            file.save(file_path)
            return 'File uploaded successfully!'
        else:
            return 'Invalid file type.', 400
    else:
        return 'No file uploaded.', 400

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File is too large. Maximum size is 5 MB.', 413

if __name__ == '__main__':
    # สร้างโฟลเดอร์ uploads ถ้ายังไม่มี
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
