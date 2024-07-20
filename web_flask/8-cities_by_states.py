#!/usr/bin/python3
""" list cities by states """
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


def bubble_sort():
    ''' retrieve and sort states and cities by name '''
    states = list(storage.all(State).values())
    n = len(states)
    for i in range(n):
        for j in range(0, n - i - 1):
            if states[j].name > states[j + 1].name:
                states[j], states[j + 1] = states[j + 1], states[j]
    sorted_states = states
    return sorted_states


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    all_citiesBYstates = bubble_sort()
    return render_template('8-cities_by_states.html',
                           states=all_citiesBYstates)


@app.teardown_appcontext
def teardown(exception):
    """ remove current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
