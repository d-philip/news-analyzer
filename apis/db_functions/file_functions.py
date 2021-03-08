import logging
import requests
from datetime import datetime
from string import ascii_lowercase
import uuid
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')
bucket = s3.Bucket('ec500-news')
table = dynamodb.Table('ec500-users')

# ----------------------------------------------------------------------------------
# File DB Functions
# ----------------------------------------------------------------------------------

def upload_file(email, file_info):
    file_id = str(uuid.uuid4())
    new_file = {
                "file_name": file_info["file_name"],
                "file_source": file_info["file_source"],
                "file_content": "",
                "upload_time": str(datetime.now()),
                "modified_time": str(datetime.now()),
                "file_keywords": [],
                "file_sentiment": None
                }

    if (new_file["file_source"] == "disk"):
        new_file["file_extension"] = file_info["file_extension"]
    elif (new_file["file_source"] == "url"):
        new_file["file_url"] = file_info["url"]

    try:
        db_resp = table.update_item(
            Key={"email": email},
            UpdateExpression="set files.#id = :f",
            ExpressionAttributeNames={"#id": file_id},
            ExpressionAttributeValues={":f": new_file},
        )

        nlp_api_url = 'http://127.0.0.1:7000/extractText'
        resp = requests.post(nlp_api_url, files={'file': file_info["raw_file"], 'email': (None, email), 'file_id': (None, file_id)})

        if (resp.status_code != 200):
            return None

        # reformat the email because the '@' character requires special handling
        email_split = email.split('@')
        file_path = email_split[0] + '_' + email_split[1] + '/' + file_id + '.pdf'
        bucket.Object(file_path).put(Body=file_info["raw_file"])

        return True
    except:
        logging.exception("Exception occurred.")
        return False

def get_file(email, file_id=None):
    resp = table.get_item(Key={'email': email}, ProjectionExpression='files')

    if (len(resp['Item']) > 0):
        files_list = resp['Item']['files']
    else:
        return None

    if (file_id is None):
        return files_list
    else:
        try:
            req_file = files_list[file_id]
            # email_split = email.split('@')
            # file_path = email_split[0] + '_' + email_split[1] + '/' + file_id + '.pdf'
            # raw_file = bucket.Object(file_path).get()['Body'].read()
            return req_file
        except:
            logging.exception("Exception occurred")
            return None

def update_file(email, file_id, updated_info):
    # define which fields the user should be unable to edit
    IMMUTABLE_KEYS = ['file_id', 'file_source', 'upload_time', 'file_extension']

    # initialize variables needed for update_item()
    attr_vals = {}
    update_expr = 'set '
    condition_expr = ''
    i = 0

    try:
        updated_info["modified_time"] = str(datetime.now())
        keys = updated_info.keys()

        # create update expression and expression attribute values object
        for key in keys:
            if (key in IMMUTABLE_KEYS):
                i += 1
                continue
            attr_str = ':' + ascii_lowercase[i]
            temp_expr = 'files.' + '#id' + '.' + key + '=' + attr_str + ','
            update_expr += temp_expr
            attr_vals[attr_str] = updated_info[key]
            i += 1
            # condition_expr += 'attribute_exists(' + key + ')' # TODO: limit updates to existing attributes

        # remove last comma from update expression
        update_expr = update_expr[:-1]

        resp = table.update_item(
            Key={'email': email},
            UpdateExpression=update_expr,
            ExpressionAttributeNames={"#id": file_id},
            ExpressionAttributeValues=attr_vals,
        )
        return True
    except:
        logging.exception("Exception occurred")
        return False

def delete_file(email, file_id):
    try:
        email_split = email.split('@')
        file_path = email_split[0] + '_' + email_split[1] + '/' + file_id + '.pdf'

        s3_resp = bucket.delete_objects(
            Delete={
                'Objects': [{
                    'Key': file_path
                }]
            })

        db_resp = table.update_item(
            Key={'email': email},
            UpdateExpression="remove files.#id",
            ExpressionAttributeNames={"#id": file_id},
        )
        return True
    except:
        logging.exception("Exception occurred")
        return False
