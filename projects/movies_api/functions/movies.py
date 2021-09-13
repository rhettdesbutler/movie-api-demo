from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


class RegisterMovie:
    def __init__(self, _id, movie_name, release_year, genre):
        self.id = _id
        self.movie_name = movie_name
        self.release_year = release_year
        self.genre = genre

    @classmethod
    def add_single_movie(cls, movie_name, release_year, genre):
        cur = mysql.connection.cursor()
        response = cur.execute(
            "INSERT INTO movies(movie_name, release_year, genre) VALUES (%s, %s, %s)", (movie_name, release_year, genre))
        mysql.connection.commit()
        cur.close()

        print(response)
        return response


class GetMovie:
    def __init__(self, _id, movie_name, release_year, genre):
        self.id = _id
        self.movie_name = movie_name
        self.release_year = release_year
        self.genre = genre

    @classmethod
    def retrieve_movie_from_name(cls, movie_name):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM movies WHERE movie_name=%s",  (movie_name,))

        movie_tuple = tuple(cur.fetchone())

        print(movie_tuple)

        if movie_tuple:
            movie = cls(*movie_tuple)
        else:
            movie = None

        cur.close()

        return movie

    @classmethod
    def retrieve_movie_from_id(cls, id):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM movies WHERE id=%s",  (id,))

        movie_tuple = tuple(cur.fetchone())

        print(movie_tuple)

        if movie_tuple:
            movie = cls(*movie_tuple)
        else:
            movie = None

        cur.close()

        return movie


class DeleteMovie:
    def __init__(self, _id, movie_name):
        self.id = _id
        self.movie_name = movie_name

    @classmethod
    def remove_single_movie(cls, movie_name):
        cur = mysql.connection.cursor()
        response = cur.execute(
            "DELETE FROM movies WHERE movie_name=%s", (movie_name, ))
        mysql.connection.commit()
        cur.close()

        print(response)
        return response
