import logging
from datetime import datetime
import uuid
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')
bucket = s3.Bucket('ec500-news')
table = dynamodb.Table('ec500-users')

# ----------------------------------------------------------------------------------
# File DB Functions
# ----------------------------------------------------------------------------------

def upload_file(email, file_info):
    new_file = [{
                "file_id": str(uuid.uuid4()),
                "file_name": file_info["file_name"],
                "file_source": file_info["file_source"],
                "file_content": "",
                "upload_time": str(datetime.now()),
                "modified_time": str(datetime.now()),
                "file_keywords": [],
                "file_sentiment": None
                }]

    if (new_file[0]["file_source"] == "disk"):
        new_file[0]["file_extension"] = file_info["file_extension"]
    elif (new_file[0]["file_source"] == "url"):
        new_file[0]["file_url"] = file_info["url"]

    try:
        # reformat the email because the '@' character requires special handling
        email_split = email.split('@')
        upload_path = email_split[0] + '_' + email_split[1] + '/' + file_info["file_name"]
        bucket.Object(upload_path).put(Body=file_info["raw_file"])

        db_resp = table.update_item(
            Key={"email": email},
            UpdateExpression="set #F = list_append(#F, :f)",
            ExpressionAttributeNames={"#F": "files"},
            ExpressionAttributeValues={":f": new_file},
        )
        return True
    except:
        return False
