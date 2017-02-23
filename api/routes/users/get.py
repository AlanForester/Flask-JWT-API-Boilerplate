from flask import Blueprint
from ...models.users import Users
from flask import request, render_template, jsonify, url_for, redirect, g
from ...services.db import db
from ...services.auth import generate_token, requires_auth, verify_token
from sqlalchemy.exc import IntegrityError

get_user_api = Blueprint('auth_api', __name__)


@get_user_api.route("/user", methods=["GET"])
@requires_auth
def get_user():
    return jsonify(result=g.current_user)
