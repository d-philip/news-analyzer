from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import db_functions as db
import json

# ----------------------------------------------------------------------------------
# User API
# ----------------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)
api = Api(app)

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
        # retrieve user info from DB
        user = db.get_user(email)

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

        # check whether or not a specific user exists in DB
        existing_user = db.get_user(email)

        if (existing_user is None):
            # add the 'new_user' object to the database
            user_created = db.create_user(user_info)
            print(user_created)

            if(user_created == True):
                return {'response': 'User data inserted successfully.'}, 201
            else:
                return {'error': 'Error creating user.'}, 404
        else:
            return {'error': 'Email is already in use.'}, 404

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
        user_exists = True              # TODO: check that a specific user exists in DB

        if (user_exists == False):
            return {"error": "User could not be found."}, 404
        else:
            for key in new_user_info:
                print(key)              # TODO: update the given fields in the DB
            return {'response': 'User info successfully changed.'}, 200

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
        user_exists = True              # TODO: check that a specific user exists in DB
        if (user_exists == False):
            return {"error": "User could not be found."}, 404
        else:
            return 204                  # TODO: remove specified user from DB

# ----------------------------------------------------------------------------------
# API Routes
# ----------------------------------------------------------------------------------
api.add_resource(User, '/users/', endpoint='users')
api.add_resource(User, '/users/<string:email>', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True)
