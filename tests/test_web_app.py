

def test_home(client):
    assert client.get('/home').status_code == 200


def test_none(client):
    assert client.get('/').status_code == 200

def test_home_contains(client):
    resp = client.get('/home')
    assert b"Hello World!" in resp.data
