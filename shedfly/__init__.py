import os
from . import web_app
from flask import Flask

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    #app = Flask(__name__, static_folder='static', static_url_path="static")
    app = Flask(__name__)

    app.register_blueprint(web_app.bp)

    return app
