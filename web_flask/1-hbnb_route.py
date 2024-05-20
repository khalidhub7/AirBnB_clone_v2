#!/usr/bin/python3
""" web_app """
from flask import FLASK
app = FLASK(__name__)


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def variable(text):
    for i in text:
        if i == '_':
            i = ' '
    return text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
