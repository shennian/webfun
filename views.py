import os
from flask import Flask, render_template, send_from_directory
from models import LoginForm, User


app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.submit() is True:
        if User(form.username, form.password).checkout():
            # login success
            pass
        else:
            # login failed
            pass
    return render_template("index.html")


@app.route('/static/<filename>', methods=['GET', 'POST'])
def send_static_file(filename):
    return send_from_directory(os.getcwd() + '/static', filename)

