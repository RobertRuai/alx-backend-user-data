#!/usr/bin/env python3
""" Flask Application """
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def message():
    """ returns json string message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """registers user if thtey dont exist"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except Exception as e:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port="5000")
