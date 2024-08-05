from flask import Flask, request, jsonify

app = Flask(__name__)

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
    
    # ไม่มีการตรวจสอบหรือการกรองข้อมูล
    with open('data.txt', 'a') as file:
        file.write(data + '\n')
    
    return 'Data submitted!'

# เส้นทางจัดการข้อผิดพลาด 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
