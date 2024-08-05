#Input Validation

from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/search" method="get">
        <input type="text" name="query" placeholder="Enter search query">
        <input type="submit" value="Search">
    </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    # ตรวจสอบว่า query เป็นข้อความที่ปลอดภัย
    if not query.isalnum():
        query = 'Invalid input'
    return render_template_string(f'''
    <h1>Search Results</h1>
    <p>You searched for: {query}</p>
    <a href="/">Back</a>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
