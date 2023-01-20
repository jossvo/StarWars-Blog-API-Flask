from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles

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
    name=request.json.get("name")
    gravity=request.json.get("gravity")
    created_by_id = request.json.get("created_by")

    new_planet = Planet(name=name,gravity=gravity,created_by_id=created_by_id)
    db.session.add(new_planet)
    db.session.commit()

    return "ok",201