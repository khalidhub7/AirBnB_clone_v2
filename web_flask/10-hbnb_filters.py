#!/usr/bin/python3
""" flask web app /hbnb_filters route """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(excpt=None):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')

