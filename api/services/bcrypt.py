from flask_bcrypt import Bcrypt
from .app import app

bcrypt = Bcrypt(app)
