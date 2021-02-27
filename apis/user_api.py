from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import requests as r

# ----------------------------------------------------------------------------------
# User API
# ----------------------------------------------------------------------------------

app = Flask(__name__)
CORS(app)
api = Api(app)

class User(Resource):
    def get(self, email=None):
        '''
        Retrieves a specified user's information from the database if an email is specified.
        If an email is not specified, retrieves a list of all users in the database.

        Parameters
        ----------
        email (optional): string
            Email of a specific user.

        Returns
        -------

        '''
        if (email is None):
            user_list = []              # TODO: retrieve list of users from DB
            return user_list, 200
        else:
            user_exists = True          # TODO: check that a specific user exists in DB

            if (user_exists == False):
                return {"error": "User could not be found."}, 404
            else:
                user_info = email       # TODO: retrieve user info
                return user_info, 200

    def post(self, user_info):
        '''
        Retrieves a new user's information from the request and adds it to the database.

        Parameters
        ----------
        user_info : JSON object
            User's information, specifically their first name, last name, and occupation.

        Returns
        -------

        '''
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
                                        # TODO: add the 'new_user' object to the database

            user_created = True         # TODO: query DB to check if user was successfully added
            if(user_created == True):
                return {'response': 'User data inserted successfully.'}, 201
            else:
                return {'error': 'Error creating user.'}, 404

    def patch(self, new_user_info):
        '''
        .

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
                                        # TODO: remove specified user from DB
            return 204

# ----------------------------------------------------------------------------------
# API Routes
# ----------------------------------------------------------------------------------
api.add_resource(User, '/users/', endpoint='users')
api.add_resource(User, '/users/<string:email>', endpoint='user')

if __name__ == '__main__':
    app.run(debug=True)
