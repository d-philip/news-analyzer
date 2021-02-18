from stub_api import *

import json

with open('users.json') as data:
    user_list = json.load(data)

user_api = User()
# ----------------------------
# User Object Tests
# ----------------------------
def get_user_test():
    assert user_api.get(user_json=user_list, email='djphilip@bu.edu') == user_list['djphilip@bu.edu'], 200
    assert user_api.get(user_json=user_list, email='elmo@gmail.com') == {"error": "User could not be found."}, 404

# def post_user_test():
#
#
# def patch_user_test():
#
#
# def delete_user_test():


# ----------------------------
# File Object Tests
# ----------------------------

# ----------------------------
# Text Analysis Tests
# ----------------------------
