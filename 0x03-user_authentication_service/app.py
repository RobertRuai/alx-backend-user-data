#!/usr/bin/env python3
""" Flask Application """
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """logins a valid user to a session"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if AUTH.valid_login(email, password) is True:
            sesh_id = AUTH.create_session(email)
            res = jsonify({"email": email, "message": "logged in"})
            res.set_cookie("session_id", sesh_id)
            return res
        abort(500)
    except Exception as e:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logsout a user"""
    sesh_id = request.cookies.get('session_id', None)
    if sesh_id is not None:
        AUTH.destroy_seseeion(sesh_id)
        return redirect(url_for(message))
    abort(403)


if __name__ == "__main__":
    """ Main Function """
    app.run(host="0.0.0.0", port="5000")
