import json
from lxml import html


def test_register_new_user(client):
    """Ensure a new user can be added to the database."""
    response = client.get('/register')
    tree = html.fromstring(response.data)
    register_token = tree.xpath('//*[@id="csrf_token"]/@value ')[0]

    response = client.post(
        '/register',
        data=json.dumps(dict(
            csrf_token=register_token,
            username='mick',
            email='mick@realpython.com',
            password='apples',
            password2='apples',
            submit='Register'
        )),
        content_type='application/json',
    )
    assert response.status_code == 302 # Found = redirect
    assert "/login" in response.location

    response = client.get(response.location)
    assert response.status_code == 200
    tree = html.fromstring(response.data)
    login_token = tree.xpath('//*[@id="csrf_token"]/@value ')[0]

    response = client.post(
        '/login',
        data=json.dumps(dict(
            csrf_token=login_token,
            username='mick',
            password='apples',
            submit='Sign In'
        )),
        content_type='application/json',
    )

    assert response.status_code == 302
    assert "/index" in response.location
    response = client.get(response.location)
    assert response.status_code == 200
    response = client.get('/logout')
    assert response.status_code == 302
    assert "/index" in response.location
    response = client.get(response.location)
    assert response.status_code == 200
