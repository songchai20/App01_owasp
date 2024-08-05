from flask import Flask, request, jsonify
import sqlite3

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
        return "No search query provided", 400

    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # การใช้ parameterized query เพื่อลดความเสี่ยงจาก SQL Injection
    cursor.execute("SELECT * FROM users WHERE username = ?", (query,))
    results = cursor.fetchall()
    conn.close()

    if not results:
        return "No results found", 404

    return str(results)

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
