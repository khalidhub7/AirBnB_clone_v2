#!/usr/bin/python3
""" web_app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    for i in text:
        if i == '_':
            i = ' '
    return 'C ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
