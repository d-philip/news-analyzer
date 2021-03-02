import logging
from datetime import datetime
import boto3
from boto3.dynamodb.conditions import Key

def create_user(user_info):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('ec500-users')

        new_user = {
                    "email": user_info['email'],
                    "first_name": user_info["first_name"],
                    "last_name": user_info["last_name"],
                    "occupation": user_info["occupation"],
                    "created": str(datetime.now()),
                    "files_url": ""
                    }

        table.put_item(Item=new_user)
        return True
    except:
        return False

def get_user(email):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ec500-users')

    resp = table.get_item(Key={'email': email})

    if 'Item' in resp:
        return resp['Item']
    else:
        return None
