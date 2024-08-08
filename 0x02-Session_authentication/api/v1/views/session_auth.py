#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    email = request.form.get('email')
    if email is None or email == '':
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None or password == '':
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except KeyError:
        return None
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for u in users:
        if u.is_valid_password(password):
            from api.v1.app import auth

            cookie_name = getenv('SESSION_NAME', None)
            session_id = auth.create_session(u.id)
            res = jsonify(u.to_json())
            res.set_cookie(cookie_name, session_id)
            return res
    return jsonify({"error": "wrong password"}), 401
