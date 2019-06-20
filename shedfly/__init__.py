import os
from . import web_app
from flask import Flask
from config import Config

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, static_folder='static_content')
    app.config.from_object(Config)
    app.register_blueprint(web_app.bp)

    return app
