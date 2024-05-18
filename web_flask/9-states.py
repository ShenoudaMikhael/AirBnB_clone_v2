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


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", defaults={"id": None}, strict_slashes=False)
def cities_by_states(id):
    """cities by states route"""

    states = storage.all(ex_models["State"])
    # print(list(states.keys()))
    if id:
        if "State.{}".format(id) in states.keys():
            return render_template(
                "9-states.html", found="Found",
                state=states["State.{}".format(id)]
            )
        else:
            print("not found")
            return render_template("9-states.html", found="NotFound")
    print("Away")

    return render_template(
        "9-states.html", found="all", states=states.values())


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
