from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles, Specie, Specie_filmography, Members_specie, Featuring_starship, Featuring_vehicle, Starship, Vehicle
from datetime import datetime

api_vehicle = Blueprint('apiVehicle', __name__)

@api_vehicle.route('/vehicle', methods=['GET'])
def vehicle():
    vehicle = Vehicle.query.all()

    response_body = list(map(lambda f: f.serialize() ,vehicle))
    return jsonify(response_body), 200

@api_vehicle.route('/vehicle/<vehicle_id>')
def get_single_vehicle(vehicle_id): 
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({"msg": "Vehiculo no encontrado"}), 404

    films = Featuring_vehicle.query.filter(Featuring_vehicle.vehicle_id==vehicle_id).all()
    films = list(map(lambda f: f.serialize_film(), films))
    pilots = Reg_vehicles.query.filter(Reg_vehicles.vehicle_id==vehicle_id).all()
    pilots = list(map(lambda p: p.serialize_pilot(), pilots))


    vehicle_json = vehicle.serialize()
    vehicle_json["films"]=films
    vehicle_json["pilots"]=pilots

    return jsonify(vehicle_json), 200

@api_vehicle.route('/vehicle', methods=['POST'])
def create_vehicle():
    class_keys = ['model', 'manufacturer', 'name', 'cost_in_credits', 'passengers', 'cargo_capacity', 'vehicle_class', 'length', 'crew', 'max_atmosphering_speed', 'url']

    new_vehicle=Vehicle()
    for key in class_keys:
        setattr(new_vehicle,key,request.json.get(key))
    setattr(new_vehicle,'edited',datetime.now())
    setattr(new_vehicle,'created',datetime.now())

    db.session.add(new_vehicle)
    db.session.commit()
    # new_vehicle = Vehicle.query.get(1)
    # class_keys = list(vars(new_vehicle).keys())
    # print(class_keys)

    return "ok",201

@api_vehicle.route('/vehicle/<vehicle_id>', methods=['PATCH'])
def update_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({"msg":"Vehiculo no encontrada"}), 404
    class_keys=['model', 'manufacturer', 'name', 'cost_in_credits', 'passengers', 'cargo_capacity', 'vehicle_class', 'length', 'crew', 'max_atmosphering_speed', 'url']
    
    for key in class_keys:
        if request.json.get(key) is not None :
            setattr(vehicle,key,request.json.get(key))
    
    setattr(vehicle,'edited',datetime.now())
    db.session.add(vehicle)
    db.session.commit()
    return jsonify(vehicle.serialize()),200

@api_vehicle.route('/vehicle/<vehicle_id>',methods=['DELETE'])
def delete_single_vehicle(vehicle_id):
    vehicle = Vehicle.query.get(vehicle_id)
    if vehicle is None:
        return jsonify({"msg":"Vehiculo no encontrada"}), 404
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify({"msg":"Vehiculo eliminada"}), 200