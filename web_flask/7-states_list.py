#!/usr/bin/python3
"""Flask App Module"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """number route"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(debug=True)
