from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    __tablename__="planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    diameter = db.Column(db.Integer(),nullable=False)
    rotation_period = db.Column(db.Integer())
    orbital_period = db.Column(db.Integer())
    gravity = db.Column(db.Float(),nullable=False)
    population = db.Column(db.Integer())
    climate = db.Column(db.String(120),nullable=False)
    terrain = db.Column(db.String(120),nullable=False)
    surface_water = db.Column(db.Integer())
    # residents = done by Table "Residents"
    # films array = done by Table "Location"
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)
    created_by_id=db.Column(db.Integer,db.ForeignKey("user.id",ondelete="cascade"))
    created_by=db.relationship(User, cascade="all, delete", passive_deletes=True)
    

    def __repr__(self):
        return '<Planet %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Specie(db.Model):
    __tablename__="specie"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    classification = db.Column(db.String(120),nullable=False)
    designation = db.Column(db.String(120),nullable=False)
    average_height = db.Column(db.String(120),nullable=False)
    average_lifespan = db.Column(db.String(120),nullable=False)
    eye_colors = db.Column(db.String(120),nullable=False)
    hair_colors = db.Column(db.String(120),nullable=False)
    skin_colors = db.Column(db.String(120),nullable=False)
    language = db.Column(db.String(120),nullable=False)
    homeworld_by_id = db.Column(db.Integer(),db.ForeignKey("planet.id",ondelete="cascade"))
    homeworld = db.relationship(Planet,cascade="all, delete", passive_deletes=True)
    # people array = done by table "Members_specie"
    # films array = done by table "specie_filmography"
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)

    def __repr__(self):
        return '<Specie %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification" : self.classification,
            "designation" : self.designation,
            "average_height" : self.average_height,
            "average_lifespan" : self.average_lifespan,
            "eye_colors" : self.eye_colors,
            "hair_colors" : self.hair_colors,
            "skin_colors" : self.skin_colors,
            "language" : self.language,
            "homeworld" : self.homeworld.name,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class People(db.Model):
    __tablename__="people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    birth_year = db.Column(db.String(120),nullable=False)
    eye_color = db.Column(db.String(120),nullable=False)
    gender = db.Column(db.String(120),nullable=False)
    hair_color = db.Column(db.String(120),nullable=False)
    height = db.Column(db.Integer())
    mass = db.Column(db.Integer())
    skin_color = db.Column(db.String(120),nullable=False)
    homeworld_by_id = db.Column(db.Integer, db.ForeignKey("planet.id",ondelete="cascade"))
    homeworld = db.relationship(Planet,cascade="all, delete", passive_deletes=True)
    # films - done by Table "Filmography"
    specie_id = db.Column(db.Integer,db.ForeignKey("specie.id",ondelete="cascade"))
    specie = db.relationship(Specie, cascade="all, delete", passive_deletes=True)
    # starships - done by table "Reg_starship"
    # vehicles - done by table "Reg_vehicle"
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)
    

    def __repr__(self):
        return '<Character %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "birth_year" : self.birth_year,
            "eye_color" : self.eye_color,
            "gender" : self.gender,
            "hair_color" : self.hair_color,
            "height" : self.height,
            "mass" : self.mass,
            "skin_color" : self.skin_color,
            "homeworld" : self.homeworld.name,
            "specie" : self.specie.name,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Film(db.Model):
    __tablename__="film"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120),nullable=False)
    episode_id = db.Column(db.Integer())
    opening_crawl = db.Column(db.String(600),nullable=False)
    director = db.Column(db.String(120),nullable=False)
    producer = db.Column(db.String(120),nullable=False)
    release_date = db.Column(db.Date(),nullable=False)
    # species array = done by table "Specie_filmography"
    # starships array = done by table "Featuring_starship"
    # vehicles array = done by table "Featuring_vehicle"
    # characters array = done by table "Filmography"
    # planets array = done by table "Location"
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)
    

    def __repr__(self):
        return '<Film %r>' % self.title
    
    def serialize(self):
        return {
            "id": self.id,
            "title" : self.title,
            "episode_id" : self.episode_id,
            "opening_crawl" : self.opening_crawl,
            "director" : self.director,
            "producer" : self.producer,
            "release_date" : self.release_date,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.title
        }

class Starship(db.Model):
    __tablename__="starship"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    model = db.Column(db.String(120),nullable=False)
    starship_class = db.Column(db.String(120),nullable=False)
    manufacturer = db.Column(db.String(120),nullable=False)
    cost_in_credits = db.Column(db.BigInteger())
    length = db.Column(db.Integer()) #float
    crew = db.Column(db.String(120),nullable=False)
    passengers = db.Column(db.Integer())
    max_atmosphering_speed = db.Column(db.Integer())
    hyperdrive_rating = db.Column(db.String(120),nullable=False)
    mglt = db.Column(db.Integer())
    cargo_capacity = db.Column(db.BigInteger())
    # films array = done by table "Featuring_starship"
    # pilots array = done by table "Reg_starship"
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)
    

    def __repr__(self):
        return '<Starship %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model" : self.model,
            "starship_class" : self.starship_class,
            "manufacturer" : self.manufacturer,
            "cost_in_credits" : self.cost_in_credits,
            "length" : self.length,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "hyperdrive_rating" : self.hyperdrive_rating,
            "mglt" : self.mglt,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited,
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Vehicle(db.Model):
    __tablename__="vehicle"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    model = db.Column(db.String(120),nullable=False)
    vehicle_class = db.Column(db.String(120),nullable=False)
    manufacturer = db.Column(db.String(120),nullable=False)
    length = db.Column(db.Integer())
    cost_in_credits = db.Column(db.BigInteger())
    crew = db.Column(db.String(120),nullable=False)
    passengers = db.Column(db.Integer())
    max_atmosphering_speed = db.Column(db.Integer())
    cargo_capacity = db.Column(db.BigInteger())
    # films array = 
    # pilots array = 
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model" : self.model,
            "vehicle_class" : self.vehicle_class,
            "manufacturer" : self.manufacturer,
            "length" : self.length,
            "cost_in_credits" : self.cost_in_credits,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "cargo_capacity" : self.cargo_capacity,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Location(db.Model):
    __tablename__="location"
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer(),db.ForeignKey("planet.id",ondelete="cascade"))
    planet = db.relationship(Planet, cascade="all, delete", passive_deletes=True)
    film_id = db.Column(db.Integer(),db.ForeignKey("film.id",ondelete="cascade"))
    film = db.relationship(Film,backref="film",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize(self):
        return {
            "film": {
                "id": self.film_id,
                "name": self.film.title
            },
            "planet": {
                "id": self.planet_id,
                "name": self.planet.name
            }
        }
    
    def serialize_movies(self):
        return self.film.serialize_simple()

    def serialize_planet(self):
        return self.planet.serialize_simple()

class Resident(db.Model):
    __tablename__="resident"
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer(),db.ForeignKey("planet.id",ondelete="cascade"))
    planet = db.relationship(Planet, cascade="all, delete", passive_deletes=True)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id",ondelete="cascade"))
    people = db.relationship(People,backref="resident",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Resident %r>' % self.people.name
    
    def serialize(self):
        return self.people.serialize_simple()

class Filmography(db.Model):
    __tablename__="filmography"
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer(),db.ForeignKey("film.id"))
    film = db.relationship(Film, cascade="all, delete", passive_deletes=True)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id",ondelete="cascade"))
    people = db.relationship(People,backref="filmography",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Filmography %r>' % self.film.title
    
    def serialize(self):
        return self.film.serialize_simple()
    def serialize_character(self):
        return self.people.serialize_simple()

class Reg_starship(db.Model):
    __tablename__="reg_starship"
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer(),db.ForeignKey("starship.id",ondelete="cascade"))
    starship = db.relationship(Starship, cascade="all, delete", passive_deletes=True)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id",ondelete="cascade"))
    people = db.relationship(People,backref="reg_starship",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Starship %r>' % self.starship.name
    
    def serialize(self):
        return self.starship.serialize_simple()
    def serialize_pilot(self):
        return self.people.serialize_simple()

class Reg_vehicles(db.Model):
    __tablename__="reg_vehicle"
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer(),db.ForeignKey("vehicle.id",ondelete="cascade"))
    vehicle = db.relationship(Vehicle, cascade="all, delete", passive_deletes=True)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id",ondelete="cascade"))
    people = db.relationship(People,backref="reg_vehicle",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle.name
    
    def serialize(self):
        return self.vehicle.serialize_simple()
    def serialize_pilot(self):
        return self.people.serialize_simple()

class Members_specie(db.Model):
    __tablename__="members_specie"
    id = db.Column(db.Integer, primary_key=True)
    specie_id = db.Column(db.Integer(),db.ForeignKey("specie.id",ondelete="cascade"))
    specie = db.relationship(Specie, cascade="all, delete", passive_deletes=True)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id",ondelete="cascade"))
    people = db.relationship(People,backref="members_specie",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Specie %r>' % self.specie.name
    
    def serialize(self):
        return self.people.serialize_simple()

class Specie_filmography(db.Model):
    __tablename__="specie_filmography"
    id = db.Column(db.Integer, primary_key=True)
    specie_id = db.Column(db.Integer(),db.ForeignKey("specie.id",ondelete="cascade"))
    specie = db.relationship(Specie, cascade="all, delete", passive_deletes=True)
    film_id = db.Column(db.Integer(),db.ForeignKey("film.id",ondelete="cascade"))
    film = db.relationship(Film,backref="specie_filmography",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize(self):
        return self.film.serialize_simple()
    def serialize_specie(self):
        return self.specie.serialize_simple()

class Featuring_starship(db.Model):
    __tablename__="featuring_starship"
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer(),db.ForeignKey("starship.id",ondelete="cascade"))
    starship = db.relationship(Starship, cascade="all, delete", passive_deletes=True)
    film_id = db.Column(db.Integer(),db.ForeignKey("film.id",ondelete="cascade"))
    film = db.relationship(Film,backref="featuring_starship",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize_starship(self):
        return self.starship.serialize_simple()
    def serialize_film(self):
        return self.film.serialize_simple()

class Featuring_vehicle(db.Model):
    __tablename__="featuring_vehicle"
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer(),db.ForeignKey("vehicle.id",ondelete="cascade"))
    vehicle = db.relationship(Vehicle, cascade="all, delete", passive_deletes=True)
    film_id = db.Column(db.Integer(),db.ForeignKey("film.id",ondelete="cascade"))
    film = db.relationship(Film,backref="featuring_vehicle",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize_vehicle(self):
        return self.vehicle.serialize_simple()
    def serialize_film(self):
        return self.film.serialize_simple()