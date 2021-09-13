
from flask import request
from flask_restful import Resource

from functions.movies import RegisterMovie, DeleteMovie, GetMovie


class AddMovie(Resource):
    def post(self):  # Specific API request
        data = request.get_json()
        movie_name = data['movie_name']
        release_year = data['release_year']
        genre = data['genre']

        try:

            RegisterMovie.add_single_movie(
                movie_name=movie_name,
                release_year=release_year,
                genre=genre
            )

        except Exception as error:
            return {"message": "Unable to add the desired movie: '{}'. Error: {}".format(movie_name, error)}, 404

        return {"message": "Movie: '{}' has successfully been added.".format(movie_name)}, 200


class RemoveMovie(Resource):

    def delete(self, movie_name):  # Specific API request

        try:

            DeleteMovie.remove_single_movie(
                movie_name=movie_name)

        except Exception as error:
            return {"message": "Unable to delete the desired movie '{}'. Error: {}".format(movie_name, error)}, 404

        return {"message": "Movie: '{}' has been deleted.".format(movie_name)}, 200


class RetrieveMovieIdByName(Resource):

    def get(self, movie_name):  # Specific API request

        try:

            movie = GetMovie.retrieve_movie_from_name(
                movie_name=movie_name
            )
            if movie == None:
                raise Exception(
                    "The movie does not exists, NoneType returned.")

        except Exception as error:
            return {"message": "Unable to retrieve the desired movie using the name '{}'. The movie does not exist. Error: {}".format(movie_name, error)}, 404

        return {"message": "The selected movie's id is: '{}'.".format(movie.id)}, 200


class RetrieveMovieNameById(Resource):

    def get(self, id):  # Specific API request

        try:
            movie = GetMovie.retrieve_movie_from_id(
                id=id)

            if movie == None:
                raise Exception(
                    " The movie does not exist, NoneType returned.")

        except Exception as error:
            return {"message": "Unable to retrieve the desired movie using id: {}. The movie does not exist. Error: {}".format(id, error)}, 404

        return {"message": "The movie name using the id {} is: '{}'.".format(id, movie.movie_name)}, 200


class RetrieveMovieByName(Resource):

    def get(self, movie_name):  # Specific API request

        try:
            movie = GetMovie.retrieve_movie_from_name(
                movie_name=movie_name)

            if movie == None:
                raise Exception("The movie does not exist, NoneType returned.")

        except Exception as error:
            return {"message": "Unable to retrieve the desired movie {}. Error: {}".format(movie_name, error)}, 404

        return {"message": "Movie name from the selected movie is: '{}'.".format(movie.movie_name)}, 200
