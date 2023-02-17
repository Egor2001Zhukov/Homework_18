# Create namespace "genres" and view
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import genre_schema, genre_service, genres_schema

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_all())

    def post(self):
        genre_service.create(genre_schema.loads(request.data))
        return 'Genre created', 201


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        return genre_schema.dump(genre_service.get_one(gid))

    def put(self, gid: int):
        genre_service.update(gid, genre_schema.loads(request.data))
        return 'Genre changed', 204

    def patch(self, gid: int):
        genre_service.partial_update(gid, genre_schema.loads(request.data))
        return 'Genre changed', 204

    def delete(self, gid: int):
        genre_service.delete(gid)
        return 'Genre deleted', 204
