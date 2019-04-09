from flask import render_template #To add tenplate
from app import app
"""
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Paul'}
    return '''
<html>
    <head>
        <title>Home Page - BLCA</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
"""

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Paul'}
    posts = [
        {
            'author': {'username': 'Jack'},
            'body': 'Next presentation'
        },
        {
            'author': {'username': 'Ben'},
            'body': 'The meeting is on Friday'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
