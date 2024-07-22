#!/usr/bin/python3
"""List cities by states."""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


def bubble_sort(states):
    """Retrieve and sort states and cities by name."""
    # Sort states
    n = len(states)
    for i in range(n):
        for j in range(0, n - i - 1):
            if states[j].name > states[j + 1].name:
                states[j], states[j + 1] = states[j + 1], states[j]

    # Sort cities within each state
    for state in states:
        state.cities = sorted(state.cities, key=lambda x: x.name)

    return states


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """Display cities by states."""
    states = list(storage.all(State).values())
    sorted_states = bubble_sort(states)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
