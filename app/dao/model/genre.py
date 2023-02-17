# Create model and Schema for it
from marshmallow import Schema, fields

from app.setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


class GenreSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()

