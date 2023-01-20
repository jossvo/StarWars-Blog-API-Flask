from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles, Specie, Specie_filmography, Members_specie
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

    filmography = Specie_filmography.query.filter(Specie_filmography.specie_id==specie_id).all()
    filmography = list(map(lambda f: f.serialize(), filmography))
    people = Members_specie.query.filter(Members_specie.specie_id==specie_id).all()
    people = list(map(lambda p: p.serialize(), people))

    specie_json = specie.serialize()
    specie_json["films"]=filmography
    specie_json["people"]=people
    return jsonify(specie_json), 200

@api_specie.route('/specie', methods=['POST'])
def create_specie():
    class_keys = [ 'classification', 'name', 'average_height', 'eye_colors', 'skin_colors', 'homeworld_by_id', 'designation', 'average_lifespan', 'hair_colors', 'language', 'url']

    new_specie=Specie()
    for key in class_keys:
        setattr(new_specie,key,request.json.get(key))
    setattr(new_specie,'edited',datetime.now())
    setattr(new_specie,'created',datetime.now())

    db.session.add(new_specie)
    db.session.commit()
    # new_specie = Specie.query.get(1)
    # class_keys = list(vars(new_specie).keys())
    # print(class_keys)

    return "ok",201

@api_specie.route('/specie/<specie_id>', methods=['PATCH'])
def update_specie(specie_id):
    specie=Specie.query.get(specie_id)
    if specie is None:
        return jsonify({"msg":"Especie no encontrada"}), 404
    class_keys=[ 'classification', 'name', 'average_height', 'eye_colors', 'skin_colors', 'homeworld_by_id', 'designation', 'average_lifespan', 'hair_colors', 'language', 'url']
    
    for key in class_keys:
        if request.json.get(key) is not None :
            setattr(specie,key,request.json.get(key))
    
    setattr(specie,'edited',datetime.now())
    db.session.add(specie)
    db.session.commit()
    return jsonify(specie.serialize()),200

@api_specie.route('/specie/<specie_id>',methods=['DELETE'])
def delete_single_specie(specie_id):
    specie = Specie.query.get(specie_id)
    if specie is None:
        return jsonify({"msg":"Especie no encontrada"}), 404
    db.session.delete(specie)
    db.session.commit()
    return jsonify({"msg":"Especie eliminada"}), 200