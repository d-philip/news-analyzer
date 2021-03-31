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
    resp1 = r.post(user_api_url, json=new_user)

    # formate request data
    document = 'tests/Salmon and Couscous Salad Recipe - NYT Cooking.pdf'
    files = {'file': open(document, 'rb'), 'source': (None, 'disk')}

    resp2 = r.post(file_api_url + 'johndoe@gmail.com/files/', files=files)
    assert resp2.json() == {'response': 'File uploaded successfully'}
    assert resp2.status_code == 200

    resp3 = r.post(file_api_url + 'janedoe@gmail.com/files/', files=files)
    assert resp3.json() == {'error': 'User could not be found.'}
    assert resp3.status_code == 404
