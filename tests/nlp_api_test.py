import requests as r
from test_config import *
from random import randint

nlp_api_url = api_url['nlp_api']
extract_url = nlp_api_url + 'extractText'
sentiment_url = nlp_api_url + 'analyzeSentiment'
keyword_url = nlp_api_url + 'generateKeywords'

email = 'ec500test@gmail.com'
file_ID1 = 'd17904d4-ca5e-4e14-ac51-83d6ef90ace7'
file_ID2 = 'bebc101f-4b25-4aa2-9c97-384035825f4d'
document1 = 'tests/Salmon and Couscous Salad Recipe - NYT Cooking.pdf'
document2 = 'tests/nonexistent.pdf'

def test_extract_text():
    resp1 = r.post(extract_url, files={'file': open(document1, 'rb'), 'email': (None, email), 'file_id': (None, file_ID1)})
    assert resp1.json() == {'response': 'Text successfully extracted and uploaded.'}
    assert resp1.status_code == 200

    resp2 = r.post(extract_url, files={'email': (None, email), 'file_id': (None, file_ID1)})
    assert resp2.json() == {'error': 'No file sent with the request.'}
    assert resp2.status_code == 400

    resp3 = r.post(extract_url, files={'file': open(document1, 'rb'), 'file_id': (None, file_ID1)})
    assert resp3.json() == {'error': 'No email sent with the request.'}
    assert resp3.status_code == 400

    resp4 = r.post(extract_url, files={'file': open(document1, 'rb'), 'email': (None, email)})
    assert resp4.json() == {'error': 'No file ID sent with the request.'}
    assert resp4.status_code == 400

    resp5 = r.post(extract_url, files={'file': open(document1, 'rb'), 'email': (None, email), 'file_id': (None, file_ID2)})
    assert resp5.json() == {'error': 'File could not be found.'}
    assert resp5.status_code == 404

def test_analyze_sentiment():
    resp1 = r.post(sentiment_url, data={'email': email, 'file_id': file_ID1})
    assert resp1.json() == {'response': 'Sentiment successfully analyzed and saved.'}
    assert resp1.status_code == 200

    resp2 = r.post(sentiment_url, data={'email': email, 'file_id': file_ID2})
    assert resp2.json() == {'error': 'File could not be found.'}
    assert resp2.status_code == 404

    resp3 = r.post(sentiment_url, data={'file_id': file_ID1})
    assert resp3.json() == {'error': 'No email sent with the request.'}
    assert resp3.status_code == 400

    resp4 = r.post(sentiment_url, data={'email': email})
    assert resp4.json() == {'error': 'No file ID sent with the request.'}
    assert resp4.status_code == 400

def test_generate_keywords():
    resp1 = r.post(keyword_url, data={'email': email, 'file_id': file_ID1})
    assert resp1.json() == {'response': 'Keywords successfully generated and saved.'}
    assert resp1.status_code == 200

    resp2 = r.post(keyword_url, data={'email': email, 'file_id': file_ID2})
    assert resp2.json() == {'error': 'File could not be found.'}
    assert resp2.status_code == 404

    resp3 = r.post(keyword_url, data={'file_id': file_ID1})
    assert resp3.json() == {'error': 'No email sent with the request.'}
    assert resp3.status_code == 400

    resp4 = r.post(keyword_url, data={'email': email})
    assert resp4.json() == {'error': 'No file ID sent with the request.'}
    assert resp4.status_code == 400
