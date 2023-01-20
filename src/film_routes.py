from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles, Specie, Specie_filmography, Members_specie
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
    species = list(map(lambda s: s.serialize(), species))
    characters = Filmography.query.filter(Filmography.film_id==film_id).all()
    characters = list(map(lambda c: c.serialize(), characters))
    planets = Location.query.filter(Location.film_id==film_id).all()
    planets = list(map(lambda p: p.serialize(), planets))

    # specie_json = specie.serialize()
    # specie_json["films"]=filmography
    # specie_json["people"]=people
    return jsonify(specie_json), 200