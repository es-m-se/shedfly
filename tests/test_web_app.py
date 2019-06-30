

def test_index(client):
    assert client.get('/index').status_code == 200

def test_none(client):
    assert client.get('/').status_code == 200

def test_index_contains(client):
    resp = client.get('/index')
    assert b"Hello World!" in resp.data

def test_style(client):
    resp = client.get('/static/main.css')
    assert b"red" in resp.data
