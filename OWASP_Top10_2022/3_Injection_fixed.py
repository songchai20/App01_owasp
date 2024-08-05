from flask import Flask, request, jsonify
import sqlite3
import re

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/search" method="get">
        <input type="text" name="query" placeholder="Enter username" required>
        <input type="submit" value="Search">
    </form>
    '''

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    # การกรองข้อมูลที่ป้อนเข้ามาเพื่อลดความเสี่ยงจาก XSS และอื่นๆ
    sanitized_query = sanitize_input(query)

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # การใช้ parameterized query เพื่อลดความเสี่ยงจาก SQL Injection
    cursor.execute("SELECT * FROM users WHERE username = ?", (sanitized_query,))
    results = cursor.fetchall()
    conn.close()

    if not results:
        return jsonify({"message": "No results found"}), 404

    return jsonify(results)

def sanitize_input(data):
    # การกรองข้อมูลที่ป้อนเข้ามา เช่น การลบตัวอักษรพิเศษที่ไม่ต้องการ
    # ในที่นี้กรองเฉพาะตัวอักษรและตัวเลข
    sanitized = re.sub(r'[^a-zA-Z0-9\s]', '', data)
    return sanitized

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
