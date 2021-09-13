from flask import request
from flask_restful import Resource

from functions.reviews import RegisterReview, DeleteReview, GetReview
from functions.movies import GetMovie
from functions.users import User


class AddReview(Resource):
    def post(self):  # Specific API request
        data = request.get_json()
        movie_name = data['movie_name']
        user_id = data['user_id']
        review = data['review']
        rating = data['rating']

        try:

            movie = GetMovie.retrieve_movie_from_name(movie_name=movie_name)

            if movie == None:
                raise Exception(
                    "No movie with the requested id is found, NoneType returned. Cannot post a review for movies that do not exist.")

        except Exception as error:
            return {"message": "Unable to locate the desired movie '{}' to add a review. Error: {}".format(movie_name, error)}, 404

        movie_id = movie.id

        try:

            RegisterReview.add_single_review(
                movie_id=movie_id,
                user_id=user_id,
                rating=rating,
                review=review
            )
        except Exception as error:
            return {"message": "Unable to add a review for '{}' .for user {}. Error: {}".format(movie_name, user_id, error)}, 404

        return {"message": "Review for movie '{}' has been added.".format(movie_name)}, 200


class RemoveReview(Resource):
    def delete(self):  # Specific API request
        data = request.get_json()
        movie_id = data['movie_id']
        user_id = data['user_id']

        try:
            delete_review_response = DeleteReview.remove_single_review(
                movie_id=movie_id,
                user_id=user_id
            )

        except Exception as error:
            return {"message": "Unable to delete the desired review, for movie (id) {} by user (id) {}. Error: {}".format(movie_id, user_id, error)}, 404

        return {"message": "Review for the movie (id) {} has been deleted for user (id): {}, response: {}.".format(movie_id, user_id, delete_review_response)}, 200


class RetrieveReview(Resource):
    def get(self):  # Specific API request
        data = request.get_json()
        movie_id = data['movie_id']
        user_email = data['email']

        try:
            user = User.find_by_user_email(
                email=user_email
            )

            if user == None:
                raise Exception(
                    "The requested user does not exist. NoneType returned.")

        except Exception as error:
            return {"message": "Unable to locate the desired movie review, for movie (id) {} and user (email) {}. Error: {}".format(movie_id, user_email, error)}, 404

        user_id = user.id

        try:
            review = GetReview.retrieve_single_review(
                movie_id=movie_id,
                user_id=user_id
            )

            if review == None:
                raise Exception("The requested review does not exist.")

        except Exception as error:
            return {"message": "Unable to locate the desired movie review, for movie (id) {} and user (id) {}. Error: {}".format(movie_id, user_id, error)}, 404

        try:
            movie = GetMovie.retrieve_movie_from_id(id=movie_id)

            if movie == None:
                raise Exception("Movie does not exists, NoneType returned")

        except Exception as error:
            {"message": "Unable to locate the desired movie (id) {} data. Error: ".format(
                movie_id, error)}, 404

        return {"message": "Found the review (id) requested: {}, posted by user: {}, movie_id: {}, movie_name: '{}', review: '{}', rating: '{}'.".format(review.id, user.email, review.movie_id, movie.movie_name, review.review, review.rating)}, 200
