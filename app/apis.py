from app import app
from flask import Flask, jsonify, request, Blueprint
from .models import db, User, Planet, Character, FavoriteCharacter, FavoritePlanet

@app.route('/users', methods=['GET'])
def getUser():
   result = User.query.all()
   data = list(map(lambda dataUser: dataUser.serialize(), result))
   return jsonify(data), 200

@app.route('/characters', methods=['GET'])
def getCharacter():
   result = Character.query.all()
   data = list(map(lambda dataUser: dataUser.serialize(), result))
   return jsonify(data), 200

@app.route('/planets', methods=['GET'])
def getPlanet():
   result = Planet.query.all()
   data = list(map(lambda dataUser: dataUser.serialize(), result))
   return jsonify(data), 200

@app.route('/favorite/characters', methods=['POST'])
def saveFavoriteCharacter():
   data_request = request.get_json()
   result = FavoriteCharacter(characters_id=data_request['characters_id'],create_at=data_request['create_at'])
   db.session.add(result)
   db.session.commit()
   return jsonify("favorite character successfully created"), 200

@app.route('/favorite/characters/<int:id>', methods=['DELETE'])
def deleteFavoriteCharacter(id):
   print(id,'aloha')
   deleteFavorite = FavoriteCharacter.query.filter_by(id=id).first()
   if not deleteFavorite:
      return jsonify({'message': 'Id not found'})
   db.session.delete(deleteFavorite)
   db.session.commit()
   return jsonify({'message': 'The favorite has been deleted'})

@app.route('/favorite/planets', methods=['POST'])
def saveFavoritePlanet():
   data_request = request.get_json()
   result = FavoritePlanet(planets_id=data_request['planets_id'],create_at=data_request['create_at'])
   db.session.add(result)
   db.session.commit()
   return jsonify("favorite planets successfully created"), 200

@app.route('/favorite/planets/<int:id>', methods=['DELETE'])
def deleteFavoritePlanet(id):
   print(id,'aloha')
   deleteFavorite = FavoritePlanet.query.filter_by(id=id).first()
   if not deleteFavorite:
      return jsonify({'message': 'Id not found'})
   db.session.delete(deleteFavorite)
   db.session.commit()
   return jsonify({'message': 'The favorite has been deleted'})