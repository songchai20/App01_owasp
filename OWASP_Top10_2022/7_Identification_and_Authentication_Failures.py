from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # ไม่มีการตรวจสอบความถูกต้องของข้อมูลการเข้าสู่ระบบ
    return f'Logged in as {username}'

if __name__ == '__main__':
    app.run(debug=True)
