import requests as r
from test_config import *

user_api_url = api_url['user_api'] + 'users/'
file_api_url = api_url['file_api'] + 'users/'

def test_post_file():
    # create test user
    new_user = {
                  "email": "johndoe@gmail.com",
                  "first_name": "John",
                  "last_name": "Doe",
                  "occupation": "baker"
                }
    r.post(user_api_url, json=new_user)

    # formate request data
    document1 = 'tests/Salmon and Couscous Salad Recipe - NYT Cooking.pdf'
    files1 = {'file': open(document1, 'rb'), 'source': (None, 'disk')}
    document2 = 'tests/applesauce.txt'
    files2 = {'file': open(document2, 'rb'), 'source': (None, 'disk')}
    files3 = {'source': (None, 'disk')}
    files4 = {'file': open(document2, 'rb')}

    resp2 = r.post(file_api_url + 'johndoe@gmail.com/files/', files=files1)
    assert resp2.json() == {'response': 'File uploaded successfully'}
    assert resp2.status_code == 200

    resp3 = r.post(file_api_url + 'janedoe@gmail.com/files/', files=files1)
    assert resp3.json() == {'error': 'User could not be found.'}
    assert resp3.status_code == 404

    resp4 = r.post(file_api_url + 'johndoe@gmail.com/files/', files=files2)
    assert resp4.json() == {'error': 'File type not supported.'}
    assert resp4.status_code == 400

    resp5 = r.post(file_api_url + 'johndoe@gmail.com/files/', files=files3)
    assert resp5.json() == {'error': 'No file sent with the request.'}
    assert resp5.status_code == 400

    resp6 = r.post(file_api_url + 'johndoe@gmail.com/files/', files=files4)
    assert resp6.json() == {'error': 'No source sent with the request.'}
    assert resp6.status_code == 400

    r.delete(user_api_url + 'johndoe@gmail.com')
