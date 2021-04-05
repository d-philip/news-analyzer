import stub_api
import json

# initialize test data and API instancess
with open('tests/users.json') as data:
    user_list = json.load(data)
with open('tests/files.json') as data:
    file_list = json.load(data)

user_api = stub_api.User()
file_api = stub_api.File()

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

def test_delete_user():
    assert user_api.delete(email='djphilip@bu.edu', user_json=user_list) == 204
    assert user_api.delete(email='applebees@gmail.com', user_json=user_list) == ({"error": "User could not be found."}, 404)

# ----------------------------
# File Object Tests
# ----------------------------
def test_get_file():
    id1 = "33f603cf-ac7f-4195-98a6-20ba3b910c93"
    id2 = "ae29df7d-adf1-4996-8964-1e8651c967e3"
    assert file_api.get(files_json=file_list, file_id=id1) == (file_list[id1], 200)
    assert file_api.get(files_json=file_list, file_id=id2) == ({"error": "File could not be found."}, 404)

def test_post_file():
    new_file = {
        "file_name": "A Famous Black Hole Gets a Massive Update",
        "file_source": "web",
        "file_url": "https://www.nytimes.com/2021/02/18/science/cygnus-black-hole-astronomy.html",
        "file_extension": '',
    }

    assert file_api.post(file_info=new_file, files_json=file_list) == ({'response': 'File data inserted successfully.'}, 201)

def test_patch_file():
    id1 = "33f603cf-ac7f-4195-98a6-20ba3b910c93"
    id2 = "5054eee5-2a13-4895-b7b7-c52167d92913"
    file_changes = {
        "file_name": "Haiku Example",
        "sentiment": 0
    }

    assert file_api.patch(new_file_info=file_changes, file_id=id1, files_json=file_list) == ({'response': 'File info successfully changed.'}, 200)
    assert file_api.patch(new_file_info=file_changes, file_id=id2, files_json=file_list) == ({"error": "File could not be found."}, 404)

def test_delete_file():
    id1 = "d914350c-e3fb-442d-8856-25b45dccb1ae"
    id2 = "c0c298af-7b8c-437d-a7a8-d84c7ddb93b3"

    assert file_api.delete(file_id=id1, files_json=file_list) == (204)
    assert file_api.delete(file_id=id2, files_json=file_list) == ({"error": "File could not be found."}, 404)
# ----------------------------
# Text Analysis Tests
# ----------------------------
