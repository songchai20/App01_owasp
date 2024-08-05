from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form.get('url')
    if not url:
        return 'No URL provided', 400

    try:
        # ช่องโหว่ SSRF (Server-Side Request Forgery)
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        return f'Error fetching URL: {e}', 500

if __name__ == '__main__':
    app.run(debug=True)
