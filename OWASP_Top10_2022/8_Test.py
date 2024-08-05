import sqlite3

def initialize_db():
    conn = sqlite3.connect('example08.db')
    cursor = conn.cursor()

    # สร้างตาราง settings หากยังไม่มี
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    ''')

    # ใส่ค่าเริ่มต้น
    cursor.execute("INSERT OR IGNORE INTO settings (key, value) VALUES ('some_key', 'default_value')")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_db()
    print("Database initialized.")
