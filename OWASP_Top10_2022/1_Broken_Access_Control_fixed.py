from flask import Flask, request, redirect, url_for, make_response, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # ใช้คีย์ลับสำหรับการจัดการเซสชัน

# ข้อมูลการเข้าสู่ระบบที่ง่ายดาย
# ใช้แฮชสำหรับรหัสผ่าน
users = {
    'admin': generate_password_hash('password123')
}

@app.route('/')
def index():
    return '''
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # ตรวจสอบผู้ใช้และรหัสผ่าน
    hashed_password = users.get(username)
    if hashed_password and check_password_hash(hashed_password, password):
        session['username'] = username
        return redirect(url_for('admin_panel'))
    
    return 'Invalid credentials', 401

@app.route('/admin')
def admin_panel():
    username = session.get('username')
    
    # ตรวจสอบการเข้าสู่ระบบและการอนุญาต
    if username == 'admin':
        return 'Welcome to the admin panel'
    
    return 'Access denied', 403

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
