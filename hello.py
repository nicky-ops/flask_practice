from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Index Page</p>'

@app.route("/about")
def about():
    return '<h1>About</h1>'

@app.route("/hello")
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{username}\'s profile'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/login')
def login():
    return 'login'


"""
URL Building
"""
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)