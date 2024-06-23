#!/usr/bin/python3
""" flask list all states """
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = sorted(storage.all('State').values(),
                    key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(current_Session):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
