from shedfly.web_app import *

def test_home():

    assert "Hello, World!" in home()
