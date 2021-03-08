from flask import Flask, request
from flask_cors import CORS
import requests as r
import json
import db_functions.log_config as log_config
import logging
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# ----------------------------------------------------------------------------------
# Text Analysis/NLP API
# ----------------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)
log_config.setup('nlp_api.log')

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
        parser = PDFParser(sent_file)
        pdf_doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        output_string = StringIO()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(pdf_doc):
            interpreter.process_page(page)
        file_text = output_string.getvalue()
    except:
        logging.exception("Exception occurred.")
        return {'error': 'Error extracting text from sent file.'}, 500

    try:
        file_api_url = 'http://127.0.0.1:5000/users/' + email + '/files/' + file_id
        print(file_id)
        resp = r.patch(file_api_url, json={'file_content': file_text})
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
    nlp_api_key = ''
    nlp_api_url = ''
    nlp_api_instance = nlp_api_url + nlp_api_key

    # TODO: check that token is valid
    req_data = request.get_json(force=True)
    req_url = 'http://localhost:5000/users/' + req_data['email'] + '/files/' + req_data['file_id']
    get_res = r.get(req_url)
    get_res_json = get_res.json()

    if get_res.status_code == 200:
        file_text = get_res_json['file_content']

        if len(file_text) < 1:
            return {'error': 'The text of the chosen file could not be retrieved, so no keywords could be generated'}, 400
        else:
            # keywords = nlp_api_instance.keywords(nlp_api_url, nlp_api_key, text)
            keywords = []
            patch_res = r.patch(req_url, data={'file_keywords': keywords})

            if patch_res.status_code == 200:
                return {'response': 'Keywords successfully generated and saved.'}, 200
            else:
                return patch_res.json()
    else:
        return get_res_json

@app.route('/analyzeSentiment', methods=['POST'])
def analyzeSentiment():
    '''
    Uses XYZ API to determine the sentiment of the text of a chosen file.

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
    req_url = 'http://localhost:5000/users/' + r.form['email'] + '/files/' + r.form['file_id']
    get_res = r.get(req_url)

    if get_res.status_code == 200:
        get_res_json = get_res.json()
        file_text = get_res_json['file_content']

        if len(file_text) < 1:
            return {'error': 'The text of the chosen file could not be retrieved, so the sentiment could not be analyzed.'}, 400
        else:
            # sentiment = nlp_api_instance.sentiment(nlp_api_url, nlp_api_key, text)
            sentiment = []
            patch_res = r.patch(req_url, data={'file_sentiment': sentiment})

            if patch_res.status_code == 200:
                return {'response': 'Sentiment successfully analyzed and saved.'}, 200
            else:
                return patch_res.json()
    else:
        return get_res_json

if __name__ == '__main__':
    app.run(debug=True)
