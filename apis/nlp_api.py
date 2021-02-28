from flask import Flask, request
from flask_cors import CORS
import requests as r
import json


# ----------------------------------------------------------------------------------
# Text Analysis/NLP API
# ----------------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)

@app.route('/generateKeywords', methods=['POST'])
def generateKeywords(text):
    '''
    Uses XYZ API to determine the keywords for the text of a chosen file.

    Parameters
    ----------
    token : string
        Authentication token of the client.
        Tokens should be passed as an HTTP Authorization header or as a POST parameter.
    file_id : integer
        ID of a specific file.
    email : string
        Email of a specific user.

    Returns
    -------

    '''
    nlp_api_key = ''
    nlp_api_url = ''
    nlp_api_instance = nlp_api_url + nlp_api_key

    # TODO: check that token is valid
    req_url = 'http://localhost:5000/users/' + email + '/files/' + file_id
    get_res = r.get(req_url)

    if get_res.status_code == 200:
        get_res_json = get_res.json()
        file_text = res_json['file_content']

        if len(file_text < 1):
            return {'error': 'The text of the chosen file could not be retrieved, thus, no keywords could be generated'}, 400
        else:
            # keywords = nlp_api_instance.keywords(nlp_api_url, nlp_api_key, text)
            keywords = []
            patch_res = r.patch(req_url, data={'file_keywords': keywords})

            if patch_res.status_code == 200:
                return 200
            else:
                return patch_res.json()
    else:
        return get_res_json


    return keywords

if __name__ == '__main__':
    app.run(debug=True)
