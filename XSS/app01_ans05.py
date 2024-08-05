#Content Security Policy (CSP)

from flask import Flask, request, render_template_string, make_response

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
    response = make_response(render_template_string(f'''
    <h1>Search Results</h1>
    <p>You searched for: {query}</p>
    <a href="/">Back</a>
    '''))
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'none';"
    return response

if __name__ == '__main__':
    app.run(debug=True)
