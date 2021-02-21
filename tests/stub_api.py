# ----------------------------------------------------------------------------------
# User Object
# ----------------------------------------------------------------------------------

class User():
    def get(self, user_json, email=None):

        if (email is None):
            return user_json
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

    def get(self, file_id=None):
        # return list of uploaded files or file with specified ID
        if (file_id is None):
            files = [] # TODO: get file objects from DB
            return {'files': files}, 200
        else:
            file = file_id # TODO: get specific file from DB
            return {'files': file}, 200

    def post(self):
        # upload file to storage system
        file_uploaded = {} # TODO: query DB to check if file was successfully added

        if(file_uploaded is not None):
            return {'response': 'File uploaded successfully.'}, 201
        else:
            return {'error': 'Error uploading file.'}, 404

    def patch(self):
        # update file attributes
        return {'response': 'File info successfully changed.'}, 200

    def delete(self, file_id):
        # delete file
        file = file_id
        # remove_file(file) # TODO: remove specified file from DB
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
