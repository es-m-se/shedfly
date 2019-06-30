import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY", default=None)
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = '5oweaZt7RMMw51LTYCzvOqfxayAkbB4AOsGTluaOP+s='
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
