from flask import request, render_template, jsonify, url_for, redirect, g
from ...models.users import Users
from ...services.auth import generate_token, requires_auth, verify_token
from flask import Blueprint
from ...services.app import app
auth_login_api = Blueprint('auth_login', __name__)


@app.route("/api/auth/login", methods=["POST"])
def authenticate():
    incoming = request.get_json()
    user = Users.get_user_with_email_and_password(incoming["email"], incoming["password"])
    if user:
        return jsonify(token=generate_token(user))

    return jsonify(error=True), 403

