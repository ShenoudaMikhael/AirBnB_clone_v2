#!/usr/bin/python3
"""Flask App Module"""
from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
