from flask import Blueprint
from ...models.users import Users
from flask import request, render_template, jsonify, url_for, redirect, g
from ...services.db import db
from ...services.auth import generate_token, requires_auth, verify_token
from sqlalchemy.exc import IntegrityError

create_user_api = Blueprint('auth_api', __name__)


@create_user_api.route("/create_user", methods=["POST"])
def create_user():
    incoming = request.get_json()
    user = Users(
        email=incoming["email"],
        password=incoming["password"]
    )
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message="User with that email already exists"), 409

    new_user = Users.query.filter_by(email=incoming["email"]).first()

    return jsonify(
        id=user.id,
        token=generate_token(new_user)
    )

