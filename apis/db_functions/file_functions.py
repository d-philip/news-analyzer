import logging
from datetime import datetime
import uuid
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
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

    # try:
    resp = table.update_item(
        Key={"email": email},
        UpdateExpression="set #F = list_append(#F, :f)",
        ExpressionAttributeNames={"#F": "files"},
        ExpressionAttributeValues={":f": new_file},
    )
    return True
    # except:
    #     return False
