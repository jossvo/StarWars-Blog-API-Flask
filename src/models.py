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
    # url string = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)
    created_by_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    created_by=db.relationship(User)
    

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

class Specie(db.Model):
    __tablename__="specie"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    classification = db.Column(db.String(120),nullable=False)
    designation = db.Column(db.String(120),nullable=False)
    average_height = db.Column(db.Integer())
    average_lifespan = db.Column(db.Integer())
    eye_colors = db.Column(db.String(120),nullable=False)
    hair_colors = db.Column(db.String(120),nullable=False)
    skin_colors = db.Column(db.String(120),nullable=False)
    language = db.Column(db.String(120),nullable=False)
    homeworld_by_id = db.Column(db.Integer(),db.ForeignKey("planet.id"))
    homeworld = db.relationship(Planet)
    # people array = 
    # films array = 
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)

    def __repr__(self):
        return '<Specie %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }

class People(db.Model):
    __tablename__="people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=False)
    birth_year = db.Column(db.Date(),nullable=False)
    eye_color = db.Column(db.String(120),nullable=False)
    gender = db.Column(db.String(120),nullable=False)
    hair_color = db.Column(db.String(120),nullable=False)
    height = db.Column(db.Integer())
    mass = db.Column(db.Integer())
    skin_color = db.Column(db.String(120),nullable=False)
    homeworld_by_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    homeworld = db.relationship(Planet)
    # films - done by Table "Filmography"
    specie_id = db.Column(db.Integer,db.ForeignKey("specie.id"))
    specie = db.relationship(Specie)
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
            "name": self.name,
            "homeworld": self.homeworld.name
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
    opening_crawl = db.Column(db.String(120),nullable=False)
    director = db.Column(db.String(120),nullable=False)
    producer = db.Column(db.String(120),nullable=False)
    release_date = db.Column(db.DateTime(),nullable=False)
    # species array = 
    # starships array = 
    # vehicles array = 
    # characters array = 
    # planets array = 
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)
    

    def __repr__(self):
        return '<Film %r>' % self.title
    
    def serialize(self):
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
    cost_in_credits = db.Column(db.Integer())
    length = db.Column(db.Integer())
    crew = db.Column(db.Integer())
    passengers = db.Column(db.Integer())
    max_atmosphering_speed = db.Column(db.Integer())
    hyperdrive_rating = db.Column(db.String(120),nullable=False)
    mglt = db.Column(db.Integer())
    cargo_capacity = db.Column(db.Integer())
    # films array = 
    # pilots array = 
    url = db.Column(db.String(120),nullable=False)
    created = db.Column(db.DateTime(),nullable=False)
    edited = db.Column(db.DateTime(),nullable=False)
    

    def __repr__(self):
        return '<Starship %r>' % self.name
    
    def serialize(self):
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
    cost_in_credits = db.Column(db.Integer())
    crew = db.Column(db.Integer())
    passengers = db.Column(db.Integer())
    max_atmosphering_speed = db.Column(db.Integer())
    cargo_capacity = db.Column(db.Integer())
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
            "name": self.name
        }

class Location(db.Model):
    __tablename__="location"
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer(),db.ForeignKey("planet.id"))
    planet = db.relationship(Planet)
    film_id = db.Column(db.Integer(),db.ForeignKey("film.id"))
    film = db.relationship(Film,backref="film",lazy=True)

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
        return self.film.serialize()

class Resident(db.Model):
    __tablename__="resident"
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer(),db.ForeignKey("planet.id"))
    planet = db.relationship(Planet)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id"))
    people = db.relationship(People,backref="resident",lazy=True)

    def __repr__(self):
        return '<Resident %r>' % self.people.name
    
    def serialize(self):
        return self.people.serialize_simple()

class Filmography(db.Model):
    __tablename__="filmography"
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer(),db.ForeignKey("film.id"))
    film = db.relationship(Film)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id"))
    people = db.relationship(People,backref="filmography",lazy=True)

    def __repr__(self):
        return '<Filmography %r>' % self.film.title
    
    def serialize(self):
        return self.film.serialize()

class Reg_starship(db.Model):
    __tablename__="reg_starship"
    id = db.Column(db.Integer, primary_key=True)
    starship_id = db.Column(db.Integer(),db.ForeignKey("starship.id"))
    starship = db.relationship(Starship)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id"))
    people = db.relationship(People,backref="reg_starship",lazy=True)

    def __repr__(self):
        return '<Starship %r>' % self.starship.name
    
    def serialize(self):
        return self.starship.serialize()

class Reg_vehicles(db.Model):
    __tablename__="reg_vehicle"
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer(),db.ForeignKey("vehicle.id"))
    vehicle = db.relationship(Vehicle)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id"))
    people = db.relationship(People,backref="reg_vehicle",lazy=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle.name
    
    def serialize(self):
        return self.vehicle.serialize()

class Members_specie(db.Model):
    __tablename__="members_specie"
    id = db.Column(db.Integer, primary_key=True)
    specie_id = db.Column(db.Integer(),db.ForeignKey("specie.id"))
    specie = db.relationship(Specie)
    people_id = db.Column(db.Integer(),db.ForeignKey("people.id"))
    people = db.relationship(People,backref="members_specie",lazy=True)

    def __repr__(self):
        return '<Specie %r>' % self.specie.name
    
    def serialize(self):
        return self.people.serialize_simple()