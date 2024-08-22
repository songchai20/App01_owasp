from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # คีย์ลับสำหรับการจัดการเซสชัน

@app.route('/')
def index():
    return '''
    <form action="/hash" method="post">
        <input type="text" name="data" placeholder="Enter data" required>
        <input type="submit" value="Hash">
    </form>
    '''

@app.route('/hash', methods=['POST'])
def hash_data():
    data = request.form.get('data')
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # ใช้ SHA-1 ซึ่งถือว่าไม่ปลอดภัย
    hashed = hashlib.sha256(data.encode()).hexdigest()
    #hashed = hashlib.md5(data.encode()).hexdigest()
    return jsonify({"hashed_data": hashed})

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
