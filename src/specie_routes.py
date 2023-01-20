from flask import Flask, Blueprint, request, jsonify
from models import db, User, Planet, People, Location, Film, Resident, Filmography, Reg_starship, Reg_vehicles, Specie
from datetime import datetime

api_specie = Blueprint('apiSpecie', __name__)

@api_specie.route('/specie', methods=['GET'])
def specie():
    specie = Specie.query.all()

    response_body = list(map(lambda s: s.serialize() ,specie))
    return jsonify(response_body), 200