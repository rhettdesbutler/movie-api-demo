from flask import Flask, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

from resources.users_resource import AddUser, ListAllUsers, RemoveUser, RetrieveUserIdByName, RetrieveUserNameById, RetrieveUserNameByName
from resources.reviews_resource import AddReview, RemoveReview, RetrieveReview
from resources.movies_resource import AddMovie, RemoveMovie, RetrieveMovieIdByName, RetrieveMovieByName, RetrieveMovieNameById

app = Flask(__name__)
app.secret_key = 'bob'
api = Api(app)

# Connection Credentials: (Should be kept in a secret)
db_hostname = "localhost"
db_password = "rhettmysql1094&"
db_username = "root"
db_name = "rhett_db"

# Database URI:
app.config['MYSQL_HOST'] = db_hostname
app.config['MYSQL_USER'] = db_username
app.config['MYSQL_PASSWORD'] = db_password
app.config['MYSQL_DB'] = db_name

mysql = MySQL(app)

# User API's
api.add_resource(AddUser, '/user/add')
api.add_resource(RemoveUser, '/user/remove/<int:id>')
api.add_resource(RetrieveUserIdByName, '/user/id/<string:name>')
api.add_resource(RetrieveUserNameById, '/user/name/<int:id>')
api.add_resource(RetrieveUserNameByName, '/user/name/<string:name>')
api.add_resource(ListAllUsers, '/users/')

# Review API's
api.add_resource(AddReview, '/review/add')
api.add_resource(RemoveReview, '/review/remove')
api.add_resource(RetrieveReview, '/review/retrieve')

# Movie API's
api.add_resource(AddMovie, '/movie/add')
api.add_resource(RemoveMovie, '/movie/remove/<string:movie_name>')
api.add_resource(RetrieveMovieIdByName, '/movie/id/<string:movie_name>')
api.add_resource(RetrieveMovieNameById, '/movie/name/<int:id>')
api.add_resource(RetrieveMovieByName, '/movie/name/<string:movie_name>')

app.run(port=5002, debug=True)
