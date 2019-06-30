import pytest
import os
import tempfile
from shedfly import create_app, db
from flask_migrate import Migrate, upgrade
from config import TestConfig

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

@pytest.yield_fixture
def client():
    """A test client for the app."""
    app = create_app(TestConfig)
    migrate = Migrate(app, db)
    with app.app_context():
        upgrade(os.path.join(basedir,'migrations'), 'head')

    with app.test_client() as client:
        yield client

    """ teardown begins """
    try:
        os.remove('/tmp/app.db')
    except:
        pass
