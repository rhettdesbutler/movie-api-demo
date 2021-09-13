from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


class User:
    def __init__(self, _id, name, email, mobile):
        self.id = _id
        self.name = name
        self.email = email
        self.mobile = mobile

    @classmethod
    def find_by_username(cls, name):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE name=%s",  (name,))

        user_tuple = tuple(cur.fetchone())

        print(user_tuple)

        if user_tuple:
            user = cls(*user_tuple)
        else:
            user = None

        cur.close()

        return user

    @classmethod
    def find_by_user_id(cls, id):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE id=%s",  (id,))

        user_tuple = tuple(cur.fetchone())

        print(user_tuple)

        if user_tuple:
            user = cls(*user_tuple)
        else:
            user = None

        cur.close()

        return user

    @classmethod
    def find_by_user_email(cls, email):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE email=%s",  (email,))

        user_tuple = tuple(cur.fetchone())

        print(user_tuple)

        if user_tuple:
            user = cls(*user_tuple)
        else:
            user = None

        cur.close()

        return user


class Users:
    def __init__(self, _id, name, email, mobile):
        self.id = _id
        self.name = name
        self.email = email
        self.mobile = mobile

    @classmethod
    def find_all_users(cls):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users")

        user_tuple = tuple(cur.fetchall())
        cur.close()

        print(user_tuple)

        if user_tuple:
            list_of_users = list(user_tuple)
        else:
            list_of_users = None

        return list_of_users


class RegisterUser:
    def __init__(self, _id, name, email, mobile):
        self.id = _id
        self.name = name
        self.email = email
        self.mobile = mobile

    @classmethod
    def add_new_user(cls, name, email, mobile):

        cur = mysql.connection.cursor()
        response = cur.execute(
            "INSERT INTO users(name, email, mobile) VALUES (%s, %s, %s)", (name, email, mobile))
        mysql.connection.commit()
        cur.close()

        print(response)
        return response


class DeleteUser:
    def __init__(self, _id, name, email, mobile):
        self.id = _id
        self.name = name
        self.email = email
        self.mobile = mobile

    @classmethod
    def remove_user(cls, id):

        cur = mysql.connection.cursor()
        response = cur.execute(
            "DELETE FROM users WHERE id = %a", (id,))
        mysql.connection.commit()
        cur.close()

        print(response)
        return response
