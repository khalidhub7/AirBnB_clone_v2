#!/usr/bin/python3
""" web_app """
from flask import Flask, render_template
from werkzeug.exceptions import NotFound
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    new = 'C '
    for i in text:
        if i == '_':
            new += ' '
        else:
            new += i
    return new


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def variable_2(text):
    new = 'Python '
    for i in text:
        if i == '_':
            new += ' '
        else:
            new += i
    return new


@app.route('/number/<n>', strict_slashes=False)
def num(n):
    try:
        numm = int(n)
        return '{} is a number'.format(numm)
    except ValueError:
        raise NotFound


@app.route('/number_template/<n>', strict_slashes=False)
def num_template(n):
    try:
        numm = int(n)
        return render_template('5-number.html', n=numm)
    except ValueError:
        raise NotFound


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def num_template_odd_even(n):
    try:
        numm = int(n)
        gen = 'odd' if numm % 2 != 0 else 'even'
        return render_template('6-number_odd_or_even.html', n=numm, gen=gen)
    except ValueError:
        raise NotFound


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
