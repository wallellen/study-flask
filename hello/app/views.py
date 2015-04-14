from flask import render_template

from app import app


@app.route('/hello')
def hello():
    return 'Hello World'


@app.route('/hello-with-template')
def hello_with_template():
    return render_template('hello.html', title='Hello', user={'name': 'Alvin', 'gender': 'M'})