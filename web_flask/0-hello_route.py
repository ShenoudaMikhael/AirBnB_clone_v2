#!/usr/bin/python3
"""Flask App Module"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Hello HBNB! Route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True)
