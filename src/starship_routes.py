from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles, Specie, Specie_filmography, Members_specie, Featuring_starship, Featuring_vehicle, Starship
from datetime import datetime

api_starship = Blueprint('apiStarship', __name__)

@api_starship.route('/starship', methods=['GET'])
def starship():
    starship = Starship.query.all()

    response_body = list(map(lambda f: f.serialize() ,starship))
    return jsonify(response_body), 200

@api_starship.route('/starship/<starship_id>')
def get_single_starship(starship_id): 
    starship = Starship.query.get(starship_id)
    if starship is None:
        return jsonify({"msg": "Nave no encontrada"}), 404

    films = Featuring_starship.query.filter(Featuring_starship.starship_id==starship_id).all()
    films = list(map(lambda f: f.serialize_film(), films))
    pilots = Reg_starship.query.filter(Reg_starship.starship_id==starship_id).all()
    pilots = list(map(lambda p: p.serialize_pilot(), pilots))


    starship_json = starship.serialize()
    starship_json["films"]=films
    starship_json["pilots"]=pilots

    return jsonify(starship_json), 200

@api_starship.route('/starship', methods=['POST'])
def create_starship():
    class_keys = ['model', 'manufacturer', 'name', 'length', 'passengers', 'hyperdrive_rating', 'cargo_capacity','starship_class', 'cost_in_credits', 'crew', 'max_atmosphering_speed', 'mglt', 'url']

    new_starship=Starship()
    for key in class_keys:
        setattr(new_starship,key,request.json.get(key))
    setattr(new_starship,'edited',datetime.now())
    setattr(new_starship,'created',datetime.now())

    db.session.add(new_starship)
    db.session.commit()

    return "ok",201

@api_starship.route('/starship/<starship_id>', methods=['PATCH'])
def update_starship(starship_id):
    starship = Starship.query.get(starship_id)
    if starship is None:
        return jsonify({"msg":"Nave no encontrada"}), 404
    class_keys=['model', 'manufacturer', 'name', 'length', 'passengers', 'hyperdrive_rating', 'cargo_capacity','starship_class', 'cost_in_credits', 'crew', 'max_atmosphering_speed', 'mglt', 'url']
    
    for key in class_keys:
        if request.json.get(key) is not None :
            setattr(starship,key,request.json.get(key))
    
    setattr(starship,'edited',datetime.now())
    db.session.add(starship)
    db.session.commit()
    return jsonify(starship.serialize()),200

@api_starship.route('/starship/<starship_id>',methods=['DELETE'])
def delete_single_starship(starship_id):
    starship = Starship.query.get(starship_id)
    if starship is None:
        return jsonify({"msg":"Nave no encontrada"}), 404
    db.session.delete(starship)
    db.session.commit()
    return jsonify({"msg":"Nave eliminada"}), 200