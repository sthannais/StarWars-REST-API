from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firts_name = db.Column(db.String(120), unique=True, nullable=False)
    last_name = db.Column(db.String(80), unique=True, nullable=False)
    mail = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    def repr(self):
        return f"User('{self.id}','{self.firts_name}', '{self.last_name}', '{self.mail}','{self.password}')"

    def serialize(self):
        return {
            "id": self.id,
            "firts_name": self.firts_name,
            "last_name": self.last_name,
            "mail": self.mail,
            "password": self.password
        }

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(120), unique=True, nullable=False)
    hair_color  = db.Column(db.String(80), unique=True, nullable=False)
    skin_color = db.Column(db.String(80), unique=True, nullable=False)
    def repr(self):
        return f"User('{self.id}','{self.name}', '{self.height}', '{self.hair_color}','{self.skin_color}')"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
        }

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=True, nullable=False)
    terrain = db.Column(db.String(80), unique=True, nullable=False)
    populations = db.Column(db.String(80), unique=True, nullable=False)
    def repr(self):
        return f"User('{self.id}','{self.name}', '{self.rotation_period}', '{self.climate}','{self.terrain}','{self.populations}')"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "climate": self.climate,
            "terrain": self.terrain,
            "populations": self.populations
        }
class FavoriteCharacter(db.Model):
    __tablename__ = 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)
    characters_id = db.Column(db.String(120), unique=True, nullable=False)
    create_at = db.Column(db.String(80), unique=True, nullable=False)
    def repr(self):
        return f"User('{self.id}','{self.characters_id}', '{self.create_at}')"

    def serialize(self):
        return {
            "id": self.id,
            "firts_name": self.characters_id,
            "last_name": self.create_at,
        }
class FavoritePlanet(db.Model):
    __tablename__ = 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    planets_id = db.Column(db.String(120), unique=True, nullable=False)
    create_at = db.Column(db.String(80), unique=True, nullable=False)
    def repr(self):
        return f"User('{self.id}','{self.planets_id}', '{self.create_at}')"

    def serialize(self):
        return {
            "id": self.id,
            "firts_name": self.planets_id,
            "last_name": self.create_at,
        }