# from stub_api import *

import json

with open('users.json') as data:
    user_list = json.load(data)

# ----------------------------
# User Object Tests
# ----------------------------
def get_user_test():
    assert User.get('djphilip@bu.edu', user_list) == user_list['djphilip@bu.edu'], 200
    assert User.get('elmo@gmail.com', user_list) == {"error": "User could not be found."}, 404

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
