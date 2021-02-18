from stub_api import *
import json

# initialize test data and API instancess
with open('tests/users.json') as data:
    user_list = json.load(data)

user_api = User()

# ----------------------------
# User Object Tests
# ----------------------------
def test_get_user():
    assert user_api.get(user_json=user_list, email='djphilip@bu.edu') == (user_list['djphilip@bu.edu'], 200)
    assert user_api.get(user_json=user_list, email='elmo@gmail.com') == ({"error": "User could not be found."}, 404)

def test_post_user():
    new_user1 = {
                "email": "jacksmith@gmail.com",
                "first_name": "Jack",
                "last_name": "Smith",
                "occupation": "baker",
                "created": 161352396
                }
    new_user2 = {
                "email": "djphilip@bu.edu",
                "first_name": "Damani",
                "last_name": "Philip",
                "occupation": "student",
                "created": 1613614196
                }

    assert user_api.post(user_info=new_user1, user_json=user_list) == ({'response': 'User data inserted successfully.'}, 201)
    assert user_api.post(user_info=new_user2, user_json=user_list) == ({"error": "Email is already in use."}, 404)

def test_patch_user():
    profile_changes = {
        "occupation": "interior designer"
    }

    assert user_api.patch(new_user_info=profile_changes, email='johndoe@gmail.com', user_json=user_list) == ({'response': 'User info successfully changed.'}, 200)
    assert user_api.patch(new_user_info=profile_changes, email='octopus.dr@gmail.com', user_json=user_list) == ({"error": "User could not be found."}, 404)

# def test_delete_user():


# ----------------------------
# File Object Tests
# ----------------------------

# ----------------------------
# Text Analysis Tests
# ----------------------------
