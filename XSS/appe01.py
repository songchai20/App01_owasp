from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1> Exam01 XSS Vulnerability </h1>
    <form action="/search" method="get">
        <input type="text" name="query" placeholder="Enter search query">
        <input type="submit" value="Search">
    </form>
    '''

@app.route('/search')
def search():
    query = request.args.get('query', '')
    return render_template_string(f'''
    <h1>Search Results</h1>
    <p>You searched for: {query}</p>
    <script>
        alert("Reflected XSS");
    </script>
    <a href="/">Back</a>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
