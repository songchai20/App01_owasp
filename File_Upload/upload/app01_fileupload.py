from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# สร้างโฟลเดอร์ uploads ถ้ายังไม่มี
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return '''
    <h1>File Upload Vulnerabirity</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        file_path = os.path.join('uploads', file.filename)
        # ตรวจสอบว่าไฟล์มีชื่อหรือไม่
        if file.filename:
            file.save(file_path)
            return 'File uploaded successfully!'
    return 'No file uploaded or invalid file.', 400

if __name__ == '__main__':
    app.run(debug=True)
