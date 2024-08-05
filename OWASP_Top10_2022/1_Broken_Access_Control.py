from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# ข้อมูลการเข้าสู่ระบบที่ง่ายดาย
users = {'admin': 'password123'}

@app.route('/')
def index():
    return '''
    <form action="/login" method="post">
        <input type="text" name="username" placeholder="Username">
        <input type="password" name="password" placeholder="Password">
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if users.get(username) == password:
        response = redirect(url_for('admin_panel'))
        response.set_cookie('username', username)
        return response
    return 'Invalid credentials', 401

@app.route('/admin')
def admin_panel():
    username = request.cookies.get('username')
    if username == 'admin':
        return 'Welcome to the admin panel'
    return 'Access denied', 403

if __name__ == '__main__':
    app.run(debug=True)
