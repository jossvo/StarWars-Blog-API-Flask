"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    users = User.query.all()


    response_body = list(map(lambda u: u.serialize() ,users))

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def planets():
    planets = Planet.query.all()


    response_body = list(map(lambda p: p.serialize() ,planets))

    return jsonify(response_body), 200

@app.route('/planets/<planet_id>')
def get_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg":"Planeta no encontrado"}), 404
    
    return jsonify(planet.serialize()), 200

@app.route('/planets', methods=['POST'])
def create_planet():
    name=request.json.get("name")
    gravity=request.json.get("gravity")
    created_by_id = request.json.get("created_by")

    new_planet = Planet(name=name,gravity=gravity,created_by_id=created_by_id)
    db.session.add(new_planet)
    db.session.commit()

    return "ok",201

@app.route('/planets/<planet_id>', methods=['PATCH'])
def update_planet(planet_id):
    planet=Planet.query.get(planet_id)
    if planet is None:
        return jsonify({"msg":"Planeta no encontrado"}), 404
    if request.json.get("name") is not None:
        planet.name=request.json.get("name")
    if request.json.get("gravity") is not None:
        planet.gravity=request.json.get("gravity")
    if request.json.get("created_by") is not None:
        planet.created_by=request.json.get("created_by")
    
    db.session.add(planet)
    db.session.commit()
    return jsonify(planet.serialize()),200

@app.route('/planets/<planet_id>',methods=['DELETE'])
def delete_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({msg:"Planeta no encontrado"}), 404
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"msg":"Planeta eliminado"}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
