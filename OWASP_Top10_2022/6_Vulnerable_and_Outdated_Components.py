from flask import Flask

app = Flask(__name__)

@app.route('/vulnerable', methods=['GET'])
def vulnerable():
    # ใช้ไลบรารีเก่าที่มีช่องโหว่ (สมมติ)
    return 'Vulnerable component'

if __name__ == '__main__':
    app.run(debug=True)
