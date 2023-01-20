from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident
from datetime import datetime

api_planets = Blueprint('apiPlanet', __name__)

@api_planets.route('/planets', methods=['GET'])
def planets():
    planets = Planet.query.all()

    response_body = list(map(lambda p: p.serialize() ,planets))
    return jsonify(response_body), 200

@api_planets.route('/planets/<planet_id>')
def get_single_planet(planet_id): 
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg":"Planeta no encontrado"}), 404
    
    films = Location.query.filter(Location.planet_id==planet_id).all()
    films = list(map(lambda l: l.serialize_movies(),films))
    residents = Resident.query.filter(Resident.planet_id==planet_id).all()
    residents = list(map(lambda r: r.serialize(),residents))
    planet_json = planet.serialize()
    planet_json["films"]=films
    planet_json["residents"]=residents
    return jsonify(planet_json), 200

@api_planets.route('/planets', methods=['POST'])
def create_planet():
    name=request.json.get("name")
    gravity=request.json.get("gravity")
    created_by_id = request.json.get("created_by")

    new_planet = Planet(name=name,gravity=gravity,created_by_id=created_by_id)
    db.session.add(new_planet)
    db.session.commit()

    return "ok",201

@api_planets.route('/planets/<planet_id>', methods=['PATCH'])
def update_planet(planet_id):
    planet=Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg":"Planeta no encontrado"}), 404
    class_keys =list(vars(planet).keys())
    class_keys.remove('_sa_instance_state')
    class_keys.remove('created')
    class_keys.remove('edited')
    class_keys.remove('created_by_id')
    
    for key in class_keys:
        if request.json.get(key) is not None :
            setattr(planet,key,request.json.get(key))
    
    setattr(planet,'edited',datetime.now())
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize()),200

@api_planets.route('/planets/<planet_id>',methods=['DELETE'])
def delete_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({msg:"Planeta no encontrado"}), 404
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"msg":"Planeta eliminado"}), 200