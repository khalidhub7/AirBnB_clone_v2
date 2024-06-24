#!/usr/bin/python3
"""Flask application to list cities by states"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


def cities_by_states():
    """Retrieve cities by states from the database"""
    city_by_state = storage.all('State').values()
    return city_by_state


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_states():
    """Display cities by states ordered alphabetically"""
    states = cities_by_states()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
