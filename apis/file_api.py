from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests as r
import db_functions.file_functions as file_db
from db_functions.user_functions import get_user
from datetime import datetime

# ----------------------------------------------------------------------------------
# File API
# ----------------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)
api = Api(app)

class File(Resource):
    def get(self, email, file_id=None):
        '''
        Retrieves a specified user's file.
        If a file ID is not specified, retrieves all of the user's in files.

        Parameters
        ----------
        file_id (optional): integer
            ID of a specific file.

        Returns
        -------

        '''
        # check whether or not a specific user exists in DB
        existing_user = get_user(email)

        if (file_id is None):
            file_list = []              # TODO: retrieve a list of a user's files from DB
            return file_list, 200
        else:
            file_exists = True          # TODO: check for specific file in DB

            if (file_exists == False):
                return {"error": "File could not be found."}, 404
            else:
                file_obj = {}           # TODO: retrieve a specific file from the DB
                return file_obj, 200

    def post(self, email):
        '''
        Retrieves an uploaded file's information and adds it to the database.

        Parameters
        ----------
        file_info : JSON object
            File's information, including its name, source, and extension or url.

        Returns
        -------

        '''
        user = get_user(email)
        if (user is None):
            return {'error': 'User could not be found.'}, 404

        accepted_extensions = ['pdf']

        if ('file' not in request.files):
            return {'error': 'No file sent with the request.'}, 400
        if ('source' not in request.form):
            return {'error': 'No source sent with the request.'}, 400
        else:
            sent_file = request.files['file']
            source = request.form['source']
            split_filename = sent_file.filename.split('.')

            try:
                file_extension = split_filename[1]
            except:
                return {'error': 'Error with filename sent in request'}, 400

            if (source == 'disk'):
                if (file_extension not in accepted_extensions):
                    return {'error': 'File type not supported.'}, 400
                else:
                    file_info = {
                        'raw_file': sent_file,
                        'file_name': sent_file.filename,
                        'file_extension': file_extension,
                        'file_source': source
                    }
                    file_uploaded = file_db.upload_file(email, file_info)

                    if file_uploaded:
                        return {'response': 'File uploaded successfully'}, 200
                    else:
                        return {'error': 'Error uploading file.'}, 500

    def patch(self, email, file_id):
        '''
        Updates the given fields of a file's information.

        Parameters
        ----------
        file_id : integer
            ID of a specific file.
        new_file_info : JSON object
            The fields and updated values that are going to overwrite a file's existing information.

        Returns
        -------

        '''
        user_exists = True              # TODO: check that a specific user exists in DB
        file_exists = True              # TODO: check that a specific file exists in DB

        if (file_exists == False):
            return {"error": "File could not be found."}, 404
        else:
            for key in new_file_info:
                print(key)              # TODO: update the given fields in the DB
                                        # TODO: update the 'modified_time' field of the file
            return {'response': 'File info successfully changed.'}, 200

    def delete(self, email, file_id):
        '''
        Deletes a file and its information from the database.

        Parameters
        ----------
        file_id : integer
            ID of a specific file.

        Returns
        -------

        '''
        user_exists = True              # TODO: check that a specific user exists in DB
        file_exists = True              # TODO: check that a specific file exists in DB
        if (file_exists == False):
            return {"error": "File could not be found."}, 404
        else:
            return 204                  # TODO: remove specified file from DB

# ----------------------------------------------------------------------------------
# API Routes
# ----------------------------------------------------------------------------------
api.add_resource(File, '/users/<string:email>/files/', endpoint='files')
api.add_resource(File, '/users/<string:email>/files/<uuid:file_id>', endpoint='file')

if __name__ == '__main__':
    app.run(debug=True)
