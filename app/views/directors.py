# Create namespace "directors" and view
from flask import request
from flask_restx import Resource, Namespace

from app.implemented import director_service, director_schema, directors_schema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_all())

    def post(self):
        director_service.create(director_schema.loads(request.data))
        return 'Director created', 201


@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        return director_schema.dump(director_service.get_one(did))

    def put(self, did: int):
        director_service.update(did, director_schema.loads(request.data))
        return 'Director changed', 204

    def patch(self, did: int):
        director_service.partial_update(did, director_schema.loads(request.data))
        return 'Director changed', 204


    def delete(self, did: int):
        director_service.delete(did)
        return 'Director deleted', 204
