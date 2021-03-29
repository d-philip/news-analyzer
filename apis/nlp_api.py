from flask import Flask, request
from flask_cors import CORS
import requests as r
import json
import db_functions.log_config as log_config
import db_functions.nlp_functions as nlp_func
from config import api_url
import logging

# ----------------------------------------------------------------------------------
# Text Analysis/NLP API
# ----------------------------------------------------------------------------------

# Setup Flask app
app = Flask(__name__)
CORS(app)

# Setup logging
log_folder = 'logs/'    # folder must be created if it does not exist
log_filename = 'nlp_api.log'
log_config.setup(log_folder + log_filename)

@app.route('/extractText', methods=['POST'])
def extractText():
    '''
    Uses PDF Miner to extract the text of a given file.

    Parameters
    ----------
    request.data
        - file_id : string
            UUID of a specific file.
        - email : string
            Email of a specific user.

    Returns
    -------

    '''
    if ('file' not in request.files):
        return {'error': 'No file sent with the request.'}, 400
    if ('email' not in request.form):
        return {'error': 'No email sent with the request.'}, 400
    if ('file_id' not in request.form):
        return {'error': 'No file ID sent with the request.'}, 400

    try:
        sent_file = request.files['file']
        email = request.form['email']
        file_id = request.form['file_id']
        file_data = sent_file.read()
    except:
        logging.exception("Exception occurred.")
        return {'error': 'Error reading request data.'}, 500

    try:    # TODO: check for file extension to determine extraction method
        file_text = nlp_func.extract_text(sent_file)
    except:
        logging.exception("Exception occurred.")
        return {'error': 'Error extracting text from sent file.'}, 500

    try:
        file_api_url = api_url['file_api'] + 'users/' + email + '/files/' + file_id
        patch_resp = r.patch(file_api_url, json={'file_content': file_text})
        if (patch_resp.status_code != 200):
            return patch_resp.json()
    except:
        logging.exception("Exception occurred. Response: " + resp.text)
        return {'error': "Error saving the file's text to the database."}, 500

    return {'response': 'Text successfully extracted and uploaded.'}, 200

@app.route('/generateKeywords', methods=['POST'])
def generateKeywords():
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
    if ('email' not in request.form):
        return {'error': 'No email sent with the request.'}, 400
    if ('file_id' not in request.form):
        return {'error': 'No file ID sent with the request.'}, 400

    req_url = api_url['file_api'] + 'users/' + request.form['email'] + '/files/' + request.form['file_id']
    get_res = r.get(req_url)
    get_res_json = get_res.json()

    if get_res.status_code == 200:
        file_text = get_res_json['file_content']

        if len(file_text) < 1:
            return {'error': 'The text of the chosen file could not be retrieved, so no keywords could be generated'}, 400
        else:
            keywords = nlp_func.generate_keywords(file_text)

            if (keywords is None):
                return {'error': "Error generating document's keywords."}, 500
            else:
                # update the document's keywords in the database
                patch_res = r.patch(req_url, json={'file_keywords': keywords})

                if patch_res.status_code == 200:
                    return {'response': 'Keywords successfully generated and saved.'}, 200
                else:
                    return patch_res.json(), patch_res.status_code
    else:
        return get_res_json, get_res.status_code

@app.route('/analyzeSentiment', methods=['POST'])
def analyzeSentiment():
    '''
    Uses XYZ API to determine the sentiment of the text of a chosen file.

    Parameters
    ----------
    file_id : integer
        ID of a specific file.
    email : string
        Email of a specific user.

    Returns
    -------

    '''
    if ('email' not in request.form):
        return {'error': 'No email sent with the request.'}, 400
    if ('file_id' not in request.form):
        return {'error': 'No file ID sent with the request.'}, 400

    req_url = api_url['file_api'] + 'users/' + request.form['email'] + '/files/' + request.form['file_id']

    get_res = r.get(req_url)
    get_res_json = get_res.json()

    if get_res.status_code == 200:
        file_text = get_res_json['file_content']

        if len(file_text) < 1:
            return {'error': 'The text of the chosen file could not be retrieved, so the sentiment could not be analyzed.'}, 400
        else:
            # get the sentiment of the file content
            sentiment = nlp_func.analyze_sentiment(file_text)

            if (sentiment is None):
                return {'error': "Error analyzing document's sentiment."}, 500
            else:
                # update the document's sentiment in the database
                patch_res = r.patch(req_url, json={'file_sentiment': str(sentiment)})

                if patch_res.status_code == 200:
                    return {'response': 'Sentiment successfully analyzed and saved.'}, 200
                else:
                    return patch_res.json(), patch_res.status_code

    else:
        return get_res_json, get_res.status_code

if __name__ == '__main__':
    app.run(debug=True)
