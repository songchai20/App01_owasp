from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

# ตรวจสอบและกรองข้อมูล
def sanitize_input(data):
    # ใช้การกรองข้อมูลเบื้องต้น เช่น การลบตัวอักษรพิเศษที่ไม่พึงประสงค์
    # ใช้ regular expression เพื่ออนุญาตเฉพาะตัวอักษรและตัวเลข
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', data)
    return sanitized

# เส้นทางหลักที่ให้ฟอร์ม HTML สำหรับการส่งข้อมูล
@app.route('/')
def index():
    return '''
    <form action="/submit" method="post">
        <input type="text" name="data" placeholder="Enter data" required>
        <input type="submit" value="Submit">
    </form>
    '''

# เส้นทางที่รับข้อมูลจากฟอร์มและบันทึกลงในไฟล์
@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('data')
    if not data:
        return 'No data provided', 400

    # ตรวจสอบและกรองข้อมูล
    sanitized_data = sanitize_input(data)

    # ตรวจสอบสิทธิ์การเขียนไฟล์และการป้องกันการเขียนไฟล์ในที่ที่ไม่พึงประสงค์
    file_path = 'data.txt'
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'a') as file:
            file.write(sanitized_data + '\n')
        return 'Data submitted!'
    else:
        return 'Error: Unable to write to file', 500

# เส้นทางจัดการข้อผิดพลาด 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
