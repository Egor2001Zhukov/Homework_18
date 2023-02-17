# Create model and Schema for it
from marshmallow import Schema, fields

from app.setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


class DirectorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()

