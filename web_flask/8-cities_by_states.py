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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """cities by states route"""
    states = storage.all(ex_models["State"]).values()

    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
