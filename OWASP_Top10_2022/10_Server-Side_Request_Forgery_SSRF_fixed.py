from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form.get('url')
    # จำกัด URL ที่สามารถเข้าถึง
    if not url.startswith('http://example.com'):
        return 'Invalid URL', 400
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
