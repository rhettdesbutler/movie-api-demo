from flask import request
from flask_restful import Resource

from functions.users import RegisterUser, DeleteUser, User, Users


class AddUser(Resource):
    def post(self):  # Specific API request
        data = request.get_json()
        user_name = data['name']
        email = data['email']
        mobile = data['mobile']

        try:

            add_new_user_response = RegisterUser.add_new_user(
                name=user_name, email=email, mobile=mobile)

        except Exception as error:
            print(error)
            return {"message": "Unable to add user with name: '{}'. Error: {}".format(user_name, error)}, 404

        if add_new_user_response == 1:
            return {"message": "User with name: '{}' successfully added.".format(user_name)}, 200


class RemoveUser(Resource):
    def delete(self, id):  # Specific API request
        data = request.get_json()
        user_id = data['id']

        try:
            delete_response = DeleteUser.remove_user(
                id=user_id
            )

        except Exception as error:
            print(error)
            return {"message": "Unable to delete user with id: {}. Error: {}".format(id, error)}, 404

        if delete_response == 1:
            return {"message": "User with id: {} successfully deleted.".format(id)}, 200


class RetrieveUserIdByName(Resource):
    def get(self, name):  # Specific API request

        try:

            user = User.find_by_username(name)

            if user == None:
                raise Exception(
                    "There is no user with name {}, NoneType returned.".format(name))

        except Exception as error:
            print(error)
            return {"message": "User with the name {} does not exist. Error: {}".format(name, error)}, 404

        return {"message": "Found the user (id) using the name provided: {}".format(user.id)}, 200


class RetrieveUserNameById(Resource):
    def get(self, id):  # Specific API request

        try:

            user = User.find_by_user_id(id)

            if user == None:
                raise Exception(
                    "There is no user with id {}, NoneType returned.".format(id))

        except Exception as error:
            print(error)
            return {"message": "User with the id {} does not exist. Error: {}".format(id, error)}, 404

        return {"message": "Found the user (name) using the id provided: {}".format(user.name)}, 200


class RetrieveUserNameByName(Resource):
    def get(self, name):  # Specific API request

        try:

            user = User.find_by_username(name=name)

            if user == None:
                raise Exception(
                    "There is no user with name '{}', NoneType returned.".format(name))

        except Exception as error:
            print(error)
            return {"message": "User with the name '{}' does not exist. Error: {}".format(name, error)}, 404

        return {"message": "Found the user (name) using the name provided: '{}'".format(user.name)}, 200


class RetrieveUserNameByEmail(Resource):
    def get(self, email):  # Specific API request

        try:

            user = User.find_by_user_email(email=email)

            if user == None:
                raise Exception(
                    "There is no user with name '{}', NoneType returned.".format(email))

        except Exception as error:
            print(error)
            return {"message": "User with the name '{}' does not exist. Error: {}".format(email, error)}, 404

        return {"message": "Found the user (name) using the name provided: '{}'".format(user.name)}, 200


class ListAllUsers(Resource):
    def get(self):  # Specific API request

        try:

            all_users = Users.find_all_users()

            if all_users == None:
                raise Exception(
                    "No users located in the database, NoneType returned.")

        except Exception as error:
            print(error)
            return {"message": "Unable to locate all users in the database. Error: {}".format(error)}, 404

        return {"message": "All users found in the database are:{}".format(all_users)}, 200
