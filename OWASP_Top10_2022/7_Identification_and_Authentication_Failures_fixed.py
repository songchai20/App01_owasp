from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# ข้อมูลการเข้าสู่ระบบที่ง่ายดาย
users = {'admin': 'password123'}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if users.get(username) == password:
        response = redirect(url_for('welcome'))
        response.set_cookie('username', username)
        return response
    return 'Invalid credentials', 401

@app.route('/welcome', methods=['GET'])
def welcome():
    username = request.cookies.get('username')
    if username in users:
        return f'Welcome, {username}'
    return 'Access denied', 403

if __name__ == '__main__':
    app.run(debug=True)
