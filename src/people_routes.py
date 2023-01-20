from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles
from datetime import datetime

api_people = Blueprint('apiPeople', __name__)

@api_people.route('/people', methods=['GET'])
def people():
    people = People.query.all()

    response_body = list(map(lambda p: p.serialize() ,people))
    return jsonify(response_body), 200

@api_people.route('/people/<people_id>')
def get_single_person(people_id): 
    people = People.query.get(people_id)
    if people is None:
        return jsonify({"msg": "Persona no encontrada"}), 404

    filmography = Filmography.query.filter(Filmography.people_id==people_id).all()
    filmography = list(map(lambda f: f.serialize(), filmography))
    starhips = Reg_starship.query.filter(Reg_starship.people_id==people_id).all()
    starhips = list(map(lambda s: s.serialize(), starhips))
    vehicles = Reg_vehicles.query.filter(Reg_vehicles.people_id==people_id).all()
    vehicles = list(map(lambda v: v.serialize(), vehicles))

    people_json = people.serialize()
    people_json["films"]=filmography
    people_json["starships"]=starhips
    people_json["vehicles"]=vehicles
    return jsonify(people_json), 200

@api_people.route('/people', methods=['POST'])
def create_person():
    class_keys = [ 'height', 'name', 'mass', 'skin_color', 'birth_year', 'homeworld_by_id', 'eye_color', 'specie_id', 'gender', 'url', 'hair_color']

    new_person=People()
    for key in class_keys:
        setattr(new_person,key,request.json.get(key))
    setattr(new_person,'edited',datetime.now())
    setattr(new_person,'created',datetime.now())

    db.session.add(new_person)
    db.session.commit()

    return "ok",201

@api_people.route('/people/<person_id>', methods=['PATCH'])
def update_person(person_id):
    person=People.query.get(person_id)
    if person is None:
        return jsonify({"msg":"Persona no encontrada"}), 404
    class_keys=[ 'height', 'name', 'mass', 'skin_color', 'birth_year', 'homeworld_by_id', 'eye_color', 'specie_id', 'gender', 'url', 'hair_color']
    
    for key in class_keys:
        if request.json.get(key) is not None :
            setattr(person,key,request.json.get(key))
    
    setattr(person,'edited',datetime.now())
    db.session.add(person)
    db.session.commit()
    return jsonify(person.serialize()),200

@api_people.route('/people/<person_id>',methods=['DELETE'])
def delete_single_person(person_id):
    person = People.query.get(person_id)
    if person is None:
        return jsonify({"msg":"Persona no encontrada"}), 404
    db.session.delete(person)
    db.session.commit()
    return jsonify({"msg":"Persona eliminada"}), 200