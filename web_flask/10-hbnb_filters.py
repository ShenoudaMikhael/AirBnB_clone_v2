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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """cities by states route"""
    states = storage.all(ex_models["State"]).values()
    amenity = storage.all(ex_models["Amenity"]).values()

    return render_template(
        "10-hbnb_filters.html", states=states, amenity=amenity)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
