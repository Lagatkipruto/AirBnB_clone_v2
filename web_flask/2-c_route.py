#!/usr/bin/python3
"""A  script that starts a Flask web application
Routes: /: display "Hello HBNB!"
/hbnb: display "HBNB"
/c/<text>: display "C" followed by the value of the text variable
listening on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """Prints C and Replace underscores with spaces"""
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
