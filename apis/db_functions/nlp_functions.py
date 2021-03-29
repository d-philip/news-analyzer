import logging
from io import StringIO
from google.cloud import language_v1

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# Initialize Google Cloud Natural Language API client
nlp_client = language_v1.LanguageServiceClient()

def extract_text(file):
    try:
        parser = PDFParser(file)
        pdf_doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        output_string = StringIO()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(pdf_doc):
            interpreter.process_page(page)
        output_text = output_string.getvalue()
        return output_text
    except:
        logging.exception("Exception occurred.")
        return None

def analyze_sentiment(text):
    try:
        type_ = language_v1.Document.Type.PLAIN_TEXT
        document = {"content": text, "type_": type_}
        encoding_type = language_v1.EncodingType.UTF8
        client_resp = nlp_client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
        sentiment = client_resp.document_sentiment.score
        return sentiment
    except:
        logging.exception("Exception occurred.")
        return None

def generate_keywords(text):
    try:
        type_ = language_v1.Document.Type.PLAIN_TEXT
        document = {"content": text, "type_": type_}
        encoding_type = language_v1.EncodingType.UTF8
        client_resp = nlp_client.analyze_entities(request = {'document': document, 'encoding_type': encoding_type})
        keywords = []
        for word in client_resp.entities:
            keywords.append(word.name)      # TODO: narrow down the list of keywords that get returned
        print("Keywords: ", keywords)
        return keywords
    except:
        logging.exception("Exception occurred.")
        return None
