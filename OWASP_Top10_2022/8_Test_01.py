from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    # รับข้อมูลจากผู้ใช้
    data = request.form.get('data')
    
    if not data:
        return 'No data provided', 400

    # เชื่อมต่อกับฐานข้อมูล SQLite
    conn = sqlite3.connect('example08.db')
    cursor = conn.cursor()

    # ช่องโหว่: ไม่มีการตรวจสอบหรือการกรองข้อมูล
    cursor.execute(f"UPDATE settings SET value = '{data}' WHERE key = 'some_key'")
    conn.commit()
    conn.close()

    return 'Data updated successfully!'

if __name__ == '__main__':
    app.run(debug=True)
