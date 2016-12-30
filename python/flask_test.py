# Flask test

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = {'GET', 'POST'})
def home():
    return '<h1>This is Home page</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='123456':
        return '<h3>Hello, Albert!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()