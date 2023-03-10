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
from models import db
from planet_routes import api_planets
from people_routes import api_people
from specie_routes import api_specie
from film_routes import api_films
from starship_routes import api_starship
from vehicle_routes import api_vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(api_planets,url_prefix="/")
app.register_blueprint(api_people,url_prefix="/")
app.register_blueprint(api_specie,url_prefix="/")
app.register_blueprint(api_films,url_prefix="/")
app.register_blueprint(api_starship,url_prefix="/")
app.register_blueprint(api_vehicle,url_prefix="/")

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

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
