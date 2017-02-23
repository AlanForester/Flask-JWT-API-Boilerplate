from flask import request, render_template, jsonify, url_for, redirect, g
from ...services.auth import generate_token, requires_auth, verify_token
from ...services.app import app


@app.route("/api/auth/check", methods=["POST"])
def is_token_valid():
    incoming = request.get_json()
    is_valid = verify_token(incoming["token"])

    if is_valid:
        return jsonify(token_is_valid=True)
    else:
        return jsonify(token_is_valid=False), 403
