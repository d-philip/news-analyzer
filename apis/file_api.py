from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests as r
import logging
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
        email : string
            Email of a specific user.
        file_id (optional): string
            UUID of a specific file.

        Returns
        -------

        '''
        # check whether or not a specific user exists in DB
        user = get_user(email)
        if (user is None):
            return {'error': 'User could not be found.'}, 404

        if (file_id is None):
            file_list = file_db.get_file(email)
            return file_list, 200
        else:
            file = file_db.get_file(email, file_id)
            if (file is None):
                return {'error': 'File could not be found.'}, 404
            else:
                return file, 200

    def post(self, email):
        '''
        Retrieves an uploaded file's information and adds it to the database.

        Parameters
        ----------
        email : string
            Email of a specific user.
        request.files : multipart/form-data
            - file : Bytes or file-like object
                File to be updated.
            - source: string
                Source of the file; either 'disk' or 'url'.

        Returns
        -------

        '''
        # check whether or not a specific user exists in DB
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
                logging.exception("Exception occurred.")
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
        Updates the given fields of a file's metadata.

        Parameters
        ----------
        file_id : string
            UUID of a specific file.
        request.new_file_info : JSON object
            The fields to be updated and their new values.

        Returns
        -------

        '''
        # check whether or not a specific user exists in DB
        user = get_user(email)
        if (user is None):
            return {'error': 'User could not be found.'}, 404

        file = file_db.get_file(email, file_id)

        if (file is None):
            return {'error': 'File could not be found.'}, 404
        else:
            new_file_info = request.get_json(force=True)
            file_updated = file_db.update_file(email, file_id, new_file_info)
            if file_updated:
                return {'response': 'File info successfully changed.'}, 200
            else:
                return {'error': 'Error updating file.'}, 500

    def delete(self, email, file_id):
        '''
        Deletes a file and its information from the database.

        Parameters
        ----------
        email : string
            Email of a specific user.
        file_id : string
            UUID of a specific file.

        Returns
        -------

        '''
        # check whether or not a specific user exists in DB
        user = get_user(email)
        if (user is None):
            return {'error': 'User could not be found.'}, 404

        file = file_db.get_file(email, file_id)

        if (file is None):
            return {'error': 'File could not be found.'}, 404
        else:
            file_deleted = file_db.delete_file(email, file_id)
            if file_deleted:
                return 204
            else:
                return {'error': 'Error deleting file.'}, 500

# ----------------------------------------------------------------------------------
# API Routes
# ----------------------------------------------------------------------------------
api.add_resource(File, '/users/<string:email>/files/', endpoint='files')
api.add_resource(File, '/users/<string:email>/files/<string:file_id>', endpoint='file')

if __name__ == '__main__':
    app.run(debug=True)
