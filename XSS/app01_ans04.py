#Template Engine 

from flask import Flask, request, render_template

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
    return render_template('index04.html', query=query)

if __name__ == '__main__':
    app.run(debug=True)
