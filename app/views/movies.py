# Create namespace "movies" and view
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import movie_service, movie_schema, movies_schema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return movies_schema.dump(movie_service.get_all())

    def post(self):
        movie_service.create(movie_schema.loads(request.data))
        return 'Movie created', 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        return movie_schema.dump(movie_service.get_one(mid))

    def put(self, mid: int):
        movie_service.update(mid, movie_schema.loads(request.data))
        return 'Movie changed', 204

    def patch(self, mid: int):
        movie_service.partial_update(mid, movie_schema.loads(request.data))
        return 'Movie changed', 204

    def delete(self, mid: int):
        movie_service.delete(mid)
        return 'Movie deleted', 204
