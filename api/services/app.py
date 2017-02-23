from flask import Flask
from ..config import BaseConfig

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")
app.config.from_object(BaseConfig)

