from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests as r

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
        user_exists = True              # TODO: check that a specific user exists in DB
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

    def post(self, email, file_info):
        '''
        Retrieves an uploaded file's information and adds it to the database.

        Parameters
        ----------
        file_info : JSON object
            File's information, including its name, source, and extension or url.

        Returns
        -------

        '''
        user_exists = True              # TODO: check that a specific user exists in DB
        new_id = str(uuid.uuid4())      # TODO: finalize ID generation
        new_file = {
                    new_id:
                        {
                        "file_name": file_info["file_name"],
                        "file_source": file_info["file_source"],
                        "file_extension": file_info["file_extension"],
                        "file_content": "",
                        "file_url": file_info["url"],
                        "upload_time": datetime.now(),
                        "modified_time": datetime.now(),
                        "file_keywords": [],
                        "file_sentiment": None
                        }
                    }

                                        # TODO: add file to DB
        file_created = True             # TODO: query DB to check if file was successfully added
        if(file_created == True):
            return {'response': 'File data inserted successfully.'}, 201
        else:
            return {'error': 'Error creating file.'}, 404

    def patch(self, email, new_file_info):
        '''
        Updates the given fields of a file's information.

        Parameters
        ----------
        new_file_info : JSON object
            The fields and updated values that are going to overwrite a file's existing information; must include the ID of the file.

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

api.add_resource(File, '/users/<string:email>/files/', endpoint='files')
api.add_resource(File, '/users/<string:email>/files/<uuid:file_id>', endpoint='file')
