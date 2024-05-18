#!/usr/bin/python3
"""Flask App Module"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


@app.route("/", strict_slashes=False)
def hello_world():
    """Hello HBNB! Route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """HBNB route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    """C route"""
    return "C {}".format(str(text).replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text):
    """Python route"""
    return "Python {}".format(str(text).replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def hello_number(n):
    """number route"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_template(n):
    """number route"""
    return render_template("5-number.html", my_number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hello_odd_even(n):
    """number route"""
    what_is = "{} is {}".format(n, "even" if n % 2 == 0 else "odd")
    return render_template("5-number.html", my_number=what_is)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """number route"""
    a = storage.all("State").values()
    return render_template("7-states_list.html", cit=a)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
