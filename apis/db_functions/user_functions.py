import logging
from datetime import datetime
from string import ascii_lowercase
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ec500-users')

# ----------------------------------------------------------------------------------
# User DB Functions
# ----------------------------------------------------------------------------------

def create_user(user_info):
    try:
        new_user = {
                    "email": user_info['email'],
                    "first_name": user_info["first_name"],
                    "last_name": user_info["last_name"],
                    "occupation": user_info["occupation"],
                    "created": str(datetime.now()),
                    "files": []
                    }

        table.put_item(Item=new_user)
        return True

    except:
        return False

def get_user(email):
    resp = table.get_item(Key={'email': email})

    if 'Item' in resp:
        return resp['Item']
    else:
        return None

def update_user(updated_info):
    try:
        keys = updated_info.keys()
        attr_vals = {}
        update_expr = 'set '
        condition_expr = ''
        i = 0

        # create update expression and expression attribute values object
        for key in keys:
            if (key == 'created' or key == 'email'):
                i += 1
                continue
            attr_str = ':' + ascii_lowercase[i]
            temp_expr = key + '=' + attr_str + ','
            update_expr += temp_expr
            attr_vals[attr_str] = updated_info[key]
            # condition_expr += 'attribute_exists(' + key + ')' # TODO: limit updates to existing attributes
            i += 1

        # remove last comma from update expression
        update_expr = update_expr[:-1]

        resp = table.update_item(
            Key={'email': updated_info['email']},
            UpdateExpression=update_expr,
            ExpressionAttributeValues=attr_vals,
            ReturnValues="UPDATED_NEW"
        )
        return True

    except:
        raise
        return False

def delete_user(email):
    try:
        resp = table.delete_item(Key={'email': email})
        return True

    except:
        return False
