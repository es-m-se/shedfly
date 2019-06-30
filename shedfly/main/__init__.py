from flask import Blueprint

bp = Blueprint('main', __name__)

from shedfly.main import routes
