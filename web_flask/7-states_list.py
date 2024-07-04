#!/usr/bin/python3
""" flask list all states """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def list_states():
    """Fetches and renders a list of all states sorted by name."""
    all_states = storage.all(State).values()
    sorted_states = sorted(all_states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)

@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
