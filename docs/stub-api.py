class User():
    def get(self, email):
        user = email # TODO: look for specific user in DB

        if (user is None):
            return {"error": "User could not be found."}, 404
        else:
            user_info = {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'occupation': user.occupation,
                'created': user.created,
                'files': user.files
            }
            return user_info, 200

    def post(self):
        # create new user object and add to DB
        user_info = request.user_data # TODO: get user data from request
        user_created = {} # TODO: query DB to check if user was successfully added

        if(user_created is not None):
            return {'response': 'User data inserted successfully.'}, 201
        else:
            return {'error': 'Error creating user.'}, 404

    def patch(self):
        # update user attributes
        changes = request.new_data
        user_info = changes
        return {'response': 'User info successfully changed.'}, 200

    def delete(self, email):
        # delete user
        user = email
        remove_user(user) # TODO: remove specified user from DB
        return 204

# ----------------------------------------------------------------------------------

class File():

    def get(self, file_id=None):
        # return list of uploaded files or file with specified ID
        if (file_id is None):
            files = [] # TODO: get file objects from DB
            return {'files': files}, 200
        else
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
        changes = request.new_data
        user_info = changes
        return {'response': 'File info successfully changed.'}, 200

    def delete(self, file_id):
        # delete file
        file = file_id
        remove_file(file) # TODO: remove specified file from DB
        return 204

# ----------------------------------------------------------------------------------
# Text Analysis Functions

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
