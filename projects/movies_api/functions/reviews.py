from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


class GetReview:
    def __init__(self, _id, user_id, movie_id, review, rating):
        self.id = _id
        self.user_id = user_id
        self.movie_id = movie_id
        self.review = review
        self.rating = rating

    @classmethod
    def retrieve_single_review(cls, movie_id, user_id):
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM reviews WHERE movie_id=%s AND user_id=%s",  (movie_id, user_id,))

        review_tuple = tuple(cur.fetchone())

        print(review_tuple)

        if review_tuple:
            review = cls(*review_tuple)
        else:
            review = None

        cur.close()

        return review


class RegisterReview:
    def __init__(self, _id, user_id, movie_id, review, rating):
        self.id = _id
        self.user_id = user_id
        self.movie_id = movie_id
        self.review = review
        self.rating = rating

    @classmethod
    def add_single_review(cls, movie_id, user_id, review, rating):
        cur = mysql.connection.cursor()
        response = cur.execute(
            "INSERT INTO reviews(user_id, movie_id,  review, rating) VALUES (%s, %s, %s, %s)", (user_id, movie_id, review, rating))
        mysql.connection.commit()
        cur.close()

        print(response)
        return response


class DeleteReview:
    def __init__(self, _id, user_id, movie_id, review, rating):
        self.id = _id
        self.user_id = user_id
        self.movie_id = movie_id
        self.review = review
        self.rating = rating

    @classmethod
    def remove_single_review(cls, user_id, movie_id):
        cur = mysql.connection.cursor()
        response = cur.execute(
            "DELETE FROM reviews WHERE user_id=%s AND movie_id=%s", (user_id, movie_id, ))
        mysql.connection.commit()
        cur.close()

        print(response)
        return response
