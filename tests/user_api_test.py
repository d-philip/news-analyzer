import requests as r
from test_config import *
from random import randint

url = api_url['user_api'] + 'users/'
email = 'johndoe' + str(randint(0,100)) + '@gmail.com'

def test_post_user():
    new_user = {
                  "email": email,
                  "first_name": "John",
                  "last_name": "Doe",
                  "occupation": "baker"
                }

    resp1 = r.post(url, json=new_user)
    assert resp1.json() == {'response': 'User successfully created.'}
    assert resp1.status_code == 201

    resp2 = r.post(url, json=new_user)
    assert resp2.json() == {'error': 'Email is already in use.'}
    assert resp2.status_code == 400

def test_get_user():
    resp1 = r.get(url + email)
    resp1_json = resp1.json()
    assert resp1_json['email'] == email
    assert resp1_json['first_name'] == 'John'
    assert resp1_json['last_name'] == 'Doe'
    assert resp1_json['occupation'] == 'baker'
    assert resp1_json['files'] == {}
    assert resp1.status_code == 200

    resp2 = r.get(url + 'janedoe@gmail.com')
    assert resp2.json() == {"error": "User could not be found."}
    assert resp2.status_code == 404

def test_patch_user():
    new_info1 = {
        'email': email,
        'occupation': 'waiter'
    }
    new_info2 = {
        'email': 'janedoe@gmail.com',
        'occupation': 'painter'
    }

    resp1 = r.patch(url, json=new_info1)
    assert resp1.json() == {'response': 'User info successfully changed.'}
    assert resp1.status_code == 200

    resp2 = r.patch(url, json=new_info2)
    assert resp2.json() == {'error': 'User could not be found.'}
    assert resp2.status_code == 404

def test_delete_user():
    resp1 = r.delete(url + email)
    assert resp1.json() == 204

    resp2 = r.delete(url + email)
    assert resp2.json() == {'error': 'User could not be found.'}
    assert resp2.status_code == 404
