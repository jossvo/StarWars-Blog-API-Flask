from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles, Specie
from datetime import datetime

api_specie = Blueprint('apiSpecie', __name__)

@api_specie.route('/specie', methods=['GET'])
def specie():
    specie = Specie.query.all()

    response_body = list(map(lambda s: s.serialize() ,specie))
    return jsonify(response_body), 200

@api_specie.route('/specie/<specie_id>')
def get_single_specie(specie_id): 
    specie = Specie.query.get(specie_id)
    if specie is None:
        return jsonify({"msg": "Persona no encontrada"}), 404

    filmography = Filmography.query.filter(Filmography.people_id==people_id).all()
    filmography = list(map(lambda f: f.serialize(), filmography))
    starhips = Reg_starship.query.filter(Reg_starship.people_id==people_id).all()
    starhips = list(map(lambda s: s.serialize(), starhips))
    vehicles = Reg_vehicles.query.filter(Reg_vehicles.people_id==people_id).all()
    vehicles = list(map(lambda v: v.serialize(), vehicles))

    specie_json = specie.serialize()
    specie_json["films"]=filmography
    specie_json["starships"]=starhips
    specie_json["vehicles"]=vehicles
    return jsonify(people_json), 200