from flask import Flask

app = Flask(__name__)

@app.route('/log', methods=['GET'])
def log():
    # ไม่มีการเก็บบันทึกหรือเฝ้าติดตามเหตุการณ์ที่เหมาะสม
    return 'Log data'

if __name__ == '__main__':
    app.run(debug=True)
