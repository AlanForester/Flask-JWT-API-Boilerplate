from flask import Blueprint
from ..services.app import app
defaults_api = Blueprint('defaults_api', __name__)


@app.route('/', methods=['GET'])
def index():
    return "Hi"


@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return path + " not found", 404
