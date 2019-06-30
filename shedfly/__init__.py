from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static_content')
    app.config.from_object(config_class)

    from shedfly.main import bp as main_bp
    app.register_blueprint(main_bp)

    db.init_app(app)

    migrate.init_app(app, db)
    login.init_app(app)

    return app
