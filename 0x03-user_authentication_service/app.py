#!/usr/bin/python3
""" Flask Application """
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def message():
    """ returns json string message"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port="5000")
