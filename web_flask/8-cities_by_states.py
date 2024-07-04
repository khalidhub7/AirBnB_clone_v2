#!/usr/bin/python3
""" list cities by states """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


def citiesBYstates():
    """ retrieve cities by states from the database """
    all_citiesBYstates = storage.all(State).values()
    return all_citiesBYstates


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    all_states = citiesBYstates()
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def teardown(exception):
    """ remove current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
