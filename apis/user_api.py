from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import db_functions.log_config as log_config
import logging
import db_functions.user_functions as user_db
import json

# ----------------------------------------------------------------------------------
# User API
# ----------------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)
api = Api(app)
log_config.setup('user_api.log')

class User(Resource):
    def get(self, email):
        '''
        Retrieves a specified user's information from the database if an email is specified.

        Parameters
        ----------
        email (optional): string
            Email of a specific user.

        Returns
        -------

        '''
        # retrieve user info from user db
        user = user_db.get_user(email)

        if (user is None):
            return {'error': 'User could not be found.'}, 404
        else:
            return user, 200

    def post(self):
        '''
        Retrieves a new user's information from the request and adds it to the database.

        Parameters
        ----------
        user_info : JSON object
            User's information, specifically their first name, last name, and occupation.

        Returns
        -------

        '''
        user_info = request.get_json(force=True)
        email = user_info['email']

        # check whether or not a specific user exists in user db
        existing_user = user_db.get_user(email)

        if (existing_user is None):
            # add the 'new_user' object to the database
            user_created = user_db.create_user(user_info)
            print(user_created)

            if(user_created == True):
                return {'response': 'User successfully created.'}, 201
            else:
                return {'error': 'Error creating user.'}, 404
        else:
            return {'error': 'Email is already in use.'}, 400

    def patch(self):
        '''
        Updates the given fields of a user's information.

        Parameters
        ----------
        new_user_info : JSON object
            The fields and updated values that are going to overwrite a user's existing information; must include the email of the user.

        Returns
        -------

        '''
        new_user_info = request.get_json(force=True)
        email = new_user_info['email']

        # check whether or not a specific user exists in user db
        existing_user = user_db.get_user(email)

        if (existing_user is None):
            return {'error': 'User could not be found.'}, 404
        else:
            user_updated = user_db.update_user(new_user_info)
            if (user_updated):
                return {'response': 'User info successfully changed.'}, 200
            else:
                return {'error': "There was an error trying to update the user's info"}, 400

    def delete(self, email):
        '''
        Deletes a user and their information from the database.

        Parameters
        ----------
        email : string
            Email of a specific user.

        Returns
        -------

        '''
        # check whether or not a specific user exists in user db
        existing_user = user_db.get_user(email)

        if (existing_user is None):
            return {'error': 'User could not be found.'}, 404
        else:
            user_deleted = user_db.delete_user(email)
            if (user_deleted):
                return 204
            else:
                return {'error': 'Error removing user from platform.'}, 400

# ----------------------------------------------------------------------------------
# API Routes
# ----------------------------------------------------------------------------------
api.add_resource(User, '/users/', endpoint='users')
api.add_resource(User, '/users/<string:email>', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True)
