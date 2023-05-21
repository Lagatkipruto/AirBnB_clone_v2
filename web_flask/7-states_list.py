#!/usr/bin/python3
"""Close the current SQLAlchemy Session
Display a HTML page with the list of all State objects
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with the list of all State objects"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
