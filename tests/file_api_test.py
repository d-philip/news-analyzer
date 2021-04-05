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

def test_get_file():
    file_ID1 = 'd17904d4-ca5e-4e14-ac51-83d6ef90ace7'
    file_ID2 = 'bebc101f-4b25-4aa2-9c97-384035825f4d'

    resp1 = r.get(file_api_url + 'ec500test@gmail.com/files/' + file_ID1)
    resp1_json = resp1.json()
    assert resp1_json['file_name'] == 'Salmon and Couscous Salad Recipe - NYT Cooking.pdf'
    assert resp1_json['file_extension'] == 'pdf'
    assert resp1_json['file_source'] == 'disk'

    resp2 = r.get(file_api_url + 'ec500test@gmail.com/files/' + file_ID2)
    assert resp2.json() == {'error': 'File could not be found.'}
    assert resp2.status_code == 404

    resp3 = r.get(file_api_url + 'janedoe@gmail.com/files/' + file_ID1)
    assert resp3.json() == {'error': 'User could not be found.'}
    assert resp3.status_code == 404

def test_patch_file():
    file_ID1 = 'd17904d4-ca5e-4e14-ac51-83d6ef90ace7'
    file_ID2 = 'bebc101f-4b25-4aa2-9c97-384035825f4d'
    updated_info = {
        'file_sentiment': '0',
        'file_keywords': ['salmon', 'couscous', 'salad']
    }

    resp1 = r.patch(file_api_url + 'ec500test@gmail.com/files/' + file_ID1, json=updated_info)
    assert resp1.json() == {'response': 'File info successfully changed.'}
    assert resp1.status_code == 200

    resp2 = r.patch(file_api_url + 'ec500test@gmail.com/files/' + file_ID2, json=updated_info)
    assert resp2.json() == {'error': 'File could not be found.'}
    assert resp2.status_code == 404

    resp3 = r.patch(file_api_url + 'janedoe@gmail.com/files/' + file_ID1)
    assert resp3.json() == {'error': 'User could not be found.'}
    assert resp3.status_code == 404

def test_delete_file():
    document = 'tests/Wild Mushroom Tart Recipe - NYT Cooking.pdf'
    file_id2 = 'bebc101f-4b25-4aa2-9c97-384035825f4d'
    files = {'file': open(document, 'rb'), 'source': (None, 'disk')}
    r.post(file_api_url + 'ec500test@gmail.com/files/', files=files)
    get_resp = r.get(file_api_url + 'ec500test@gmail.com/files/')
    get_resp_json = get_resp.json()
    for file_id, file_info in get_resp_json.items():
        if file_info['file_name'] == 'Wild Mushroom Tart Recipe - NYT Cooking.pdf':
            file_id1 = file_id

    resp1 = r.delete(file_api_url + 'ec500test@gmail.com/files/' + file_id1)
    assert resp1.status_code == 200

    resp2 = r.delete(file_api_url + 'ec500test@gmail.com/files/' + file_id2)
    assert resp2.json() == {'error': 'File could not be found.'}
    assert resp2.status_code == 404

    resp3 = r.delete(file_api_url + 'janedoe@gmail.com/files/' + file_id1)
    assert resp3.json() == {'error': 'User could not be found.'}
    assert resp3.status_code == 404
