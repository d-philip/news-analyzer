# ----------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------
from datetime import datetime
import uuid

# ----------------------------------------------------------------------------------
# User Object
# ----------------------------------------------------------------------------------

class User():
    def get(self, user_json, email=None):

        if (email is None):
            return user_json, 200
        else:
            user_exists = email in user_json # TODO: look for specific user in DB

            if (user_exists == False):
                return {"error": "User could not be found."}, 404
            else:
                user_obj = user_json[email]
                return user_obj, 200

    def post(self, user_info, user_json):
        # create new user object and add to DB

        email = user_info['email']
        user_exists = email in user_json

        if (user_exists == True):
            return {"error": "Email is already in use."}, 404
        else:
            new_user = {
                        user_info['email']:
                            {
                            "first_name": user_info["first_name"],
                            "last_name": user_info["last_name"],
                            "occupation": user_info["occupation"],
                            "created": user_info["created"]
                            }
                        }
            user_json.update(new_user)

            user_created = email in user_json # TODO: query DB to check if user was successfully added
            if(user_created == True):
                return {'response': 'User data inserted successfully.'}, 201
            else:
                return {'error': 'Error creating user.'}, 404

    def patch(self, new_user_info, email, user_json):
        # update user attributes
        user_exists = email in user_json

        if (user_exists == False):
            return {"error": "User could not be found."}, 404
        else:
            for key in new_user_info:
                user_json[email][key] = new_user_info[key]
            return {'response': 'User info successfully changed.'}, 200

    def delete(self, email, user_json):
        # delete user
        user_exists = email in user_json
        if (user_exists == False):
            return {"error": "User could not be found."}, 404
        else:
            # remove_user(user) # TODO: remove specified user from DB
            del user_json[email]
            return 204

# ----------------------------------------------------------------------------------
# File Object
# ----------------------------------------------------------------------------------

class File():

    def get(self, files_json, file_id=None):
        # return list of uploaded files or file with specified ID
        if (file_id is None):
            # TODO: return list of a user's files
            return files_json, 200
        else:
            file_exists = file_id in files_json # TODO: look for specific file in DB

            if (file_exists == False):
                return {"error": "File could not be found."}, 404
            else:
                file_obj = files_json[file_id]
                return file_obj, 200

    def post(self, file_info, files_json):
        # upload file to storage system

        new_id = str(uuid.uuid4())
        new_file = {
                    new_id: # generate random ID
                        {
                        "file_name": file_info["file_name"],
                        "file_source": file_info["file_source"],
                        "file_extension": file_info["file_extension"],
                        "file_content": "",
                        "file_url": "",
                        "upload_time": datetime.now(),
                        "modified_time": datetime.now(),
                        "file_keywords": [],
                        "file_sentiment": None
                        }
                    }
        files_json.update(new_file)

        file_created = new_id in files_json # TODO: query DB to check if user was successfully added
        if(file_created == True):
            return {'response': 'File data inserted successfully.'}, 201
        else:
            return {'error': 'Error creating file.'}, 404

    def patch(self, new_file_info, file_id, files_json):
        # update file attributes
        file_exists = file_id in files_json

        if (file_exists == False):
            return {"error": "File could not be found."}, 404
        else:
            for key in new_file_info:
                files_json[file_id][key] = new_file_info[key]
            files_json[file_id]["modified_time"] = datetime.now()
            return {'response': 'File info successfully changed.'}, 200

    def delete(self, file_id, files_json):
        # delete file
        file_exists = file_id in files_json
        if (file_exists == False):
            return {"error": "File could not be found."}, 404
        else:
            del files_json[file_id]
            return 204

# ----------------------------------------------------------------------------------
# Text Analysis Functions
# ----------------------------------------------------------------------------------

def generateKeywords(text):
    nlp_api_key = ''
    nlp_api_url = ''
    nlp_api_instance = nlp_api_url + nlp_api_key

    keywords = nlp_api_instance.keywords(nlp_api_url, nlp_api_key, text)
    return keywords

def analyzeSentiment(text):
    nlp_api_key = ''
    nlp_api_url = ''
    nlp_api_instance = nlp_api_url + nlp_api_key

    sentiment = nlp_api_instance.sentiment(nlp_api_url, nlp_api_key, text)
    return sentiment

def translateText(text, base_language, target_language):
    nlp_api_key = ''
    nlp_api_url = ''
    nlp_api_instance = nlp_api_url + nlp_api_key

    translated_text = nlp_api_instance.translate(text, base_language, target_language)
    return translated_text
# ----------------------------------------------------------------------------------

# URL schema for reference
# - collection of files: `users/{user_id}/files`
# - individual file: `users/{user_id}/files/{file_id}`
