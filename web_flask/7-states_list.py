#!/usr/bin/python3
"""Flask App Module"""
from flask import Flask, render_template
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

app = Flask(__name__)
ex_models = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User,
}


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """states list route"""
    states = list(storage.all(ex_models["City"]).values())
    states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
