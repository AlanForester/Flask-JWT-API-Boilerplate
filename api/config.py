import os

from setup import basedir


class BaseConfig(object):
    SECRET_KEY = "SO_SECURE"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://iqfx@localhost/iqfx"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
