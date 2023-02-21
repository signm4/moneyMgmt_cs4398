from flask import Flask, render_template
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required

app = Flask(__name__)

# @app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def login():
    return render_template('login.html')

