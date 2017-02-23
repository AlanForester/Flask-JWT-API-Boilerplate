from ..services.db import db
from ..services.bcrypt import bcrypt


class Users(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.active = True
        self.password = Users.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password)

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = Users.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
