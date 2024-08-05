import sqlite3

def initialize_database():
    # เชื่อมต่อกับฐานข้อมูล (จะสร้างฐานข้อมูลใหม่หากไม่มี)
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # สร้างตาราง users หากยังไม่มี
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE
    )
    ''')

    # ลบข้อมูลเก่า (ใช้เพื่อการทดสอบใหม่)
    cursor.execute("DELETE FROM users")

    # เพิ่มข้อมูลตัวอย่าง
    cursor.execute("INSERT INTO users (username) VALUES ('testuser')")
    cursor.execute("INSERT INTO users (username) VALUES ('admin')")

    # บันทึกการเปลี่ยนแปลงและปิดการเชื่อมต่อ
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
    print("Database initialized successfully.")
