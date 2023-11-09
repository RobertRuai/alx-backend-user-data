#!/usr/bin/env python3
"""views for session_authentication"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route(
                 '/auth_session/login',
                 methods=['POST'], strict_slashes=False)
def authenticate():
    """authentication route"""
    email = request.form.get("email")
    pswd = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pswd:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(pswd):
            user_id = user.id
            from api.v1.app import auth
            sesh_id = auth.create_session(user_id)
            res = jsonify(user.to_json())
            res.set_cookie(getenv('SESSION_NAME'), sesh_id)
            return res
        else:
            return jsonify({"error": "wrong password"}), 401
    return jsonify(error="no user found for this email"), 404


@app_views.route(
                 '/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """logout route"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
