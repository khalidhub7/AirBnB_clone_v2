#!/usr/bin/python3
""" list cities by states """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


def sorted_states():
    """ retrieve and sort states and cities by name """
    all_states = storage.all(State).values()
    sorted_states = sorted(all_states, key=lambda state: state.name)
    for state in sorted_states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return sorted_states


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    all_citiesBYstates = sorted_states()
    return render_template('8-cities_by_states.html',
                           states=all_citiesBYstates)


@app.teardown_appcontext
def teardown(exception):
    """ remove current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
