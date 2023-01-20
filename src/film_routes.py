from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles, Specie, Specie_filmography, Members_specie, Featuring_starship, Featuring_vehicle
from datetime import datetime

api_films = Blueprint('apiFilms', __name__)

@api_films.route('/film', methods=['GET'])
def film():
    film = Film.query.all()

    response_body = list(map(lambda f: f.serialize() ,film))
    return jsonify(response_body), 200

@api_films.route('/film/<film_id>')
def get_single_film(film_id): 
    film = Film.query.get(film_id)
    if film is None:
        return jsonify({"msg": "Pelicula no encontrada"}), 404

    species = Specie_filmography.query.filter(Specie_filmography.film_id==film_id).all()
    species = list(map(lambda s: s.serialize_specie(), species))
    characters = Filmography.query.filter(Filmography.film_id==film_id).all()
    characters = list(map(lambda c: c.serialize_character(), characters))
    planets = Location.query.filter(Location.film_id==film_id).all()
    planets = list(map(lambda p: p.serialize_planet(), planets))
    starships = Featuring_starship.query.filter(Featuring_starship.film_id==film_id).all()
    starships = list(map(lambda s: s.serialize_starship(), starships))
    vehicles = Featuring_vehicle.query.filter(Featuring_vehicle.film_id==film_id).all()
    vehicles = list(map(lambda v: v.serialize_vehicle(), vehicles))

    film_json = film.serialize()
    film_json["species"]=species
    film_json["characters"]=characters
    film_json["planets"]=planets
    film_json["starships"]=starships
    film_json["vehicles"]=vehicles
    return jsonify(film_json), 200

@api_films.route('/film', methods=['POST'])
def create_film():
    class_keys = [ 'opening_crawl', 'producer', 'url', 'title', 'episode_id', 'director', 'release_date']

    new_film=Film()
    for key in class_keys:
        setattr(new_film,key,request.json.get(key))
    setattr(new_film,'edited',datetime.now())
    setattr(new_film,'created',datetime.now())

    db.session.add(new_film)
    db.session.commit()

    return "ok",201

@api_films.route('/film/<film_id>', methods=['PATCH'])
def update_film(film_id):
    film=Film.query.get(film_id)
    if film is None:
        return jsonify({"msg":"Pelicula no encontrada"}), 404
    class_keys=[ 'opening_crawl', 'producer', 'url', 'title', 'episode_id', 'director', 'release_date']
    
    for key in class_keys:
        if request.json.get(key) is not None :
            setattr(film,key,request.json.get(key))
    
    setattr(film,'edited',datetime.now())
    db.session.add(film)
    db.session.commit()
    return jsonify(film.serialize()),200

@api_films.route('/film/<film_id>',methods=['DELETE'])
def delete_single_film(film_id):
    film = Film.query.get(film_id)
    if film is None:
        return jsonify({"msg":"Pelicula no encontrada"}), 404
    db.session.delete(film)
    db.session.commit()
    return jsonify({"msg":"Pelicula eliminada"}), 200