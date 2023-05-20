#!/usr/bin/python3
"""A  script that starts a Flask web application
that is  listening on 0.0.0.0, port 5000
ROUTES:
  / display "Hello HBNB"
  /hbnb: display "HBNB"
  /c/<text>: display "C", followed by the value of the text variable
  /python/(<text>): display "Python",
  followed by the value of the text variable
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Print Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """display "C", followed by the value of the text variable"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Prints Python replacing _ with spaces"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
