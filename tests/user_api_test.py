import requests as r

url = "http://54.91.38.146:8080/users/"

def test_post_user():
    new_user = {
                  "email": "johndoe@gmail.com",
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
    resp1 = r.get(url + 'johndoe@gmail.com')
    resp1_json = resp1.json()
    assert resp1_json['email'] == 'johndoe@gmail.com'
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
        'email': 'johndoe@gmail.com',
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
    resp1 = r.delete(url + 'johndoe@gmail.com')
    assert resp1.json() == 204

    resp2 = r.delete(url + 'johndoe@gmail.com')
    assert resp2.json() == {'error': 'User could not be found.'}
    assert resp2.status_code == 404
