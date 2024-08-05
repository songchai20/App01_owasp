from flask import Flask, request

app = Flask(__name__)

@app.route('/update', methods=['POST'])
def update():
    data = request.form.get('data')
    # ไม่มีการตรวจสอบความถูกต้องของข้อมูลที่อัปเดต
    with open('data.txt', 'w') as file:
        file.write(data)
    return 'Data updated!'

if __name__ == '__main__':
    app.run(debug=True)
