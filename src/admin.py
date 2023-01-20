import os
from flask_admin import Admin
from models import db, User, Planet, People, Film, Starship, Vehicle, Specie, Location, Resident, Filmography, Reg_starship, Reg_vehicles, Members_specie, Specie_filmography, Featuring_starship, Featuring_vehicle
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Film, db.session))
    admin.add_view(ModelView(Starship, db.session))
    admin.add_view(ModelView(Vehicle, db.session))
    admin.add_view(ModelView(Specie, db.session))

    #Tables to connect tables
    admin.add_view(ModelView(Location, db.session))
    admin.add_view(ModelView(Resident, db.session))
    admin.add_view(ModelView(Filmography, db.session))
    admin.add_view(ModelView(Reg_starship, db.session))
    admin.add_view(ModelView(Reg_vehicles, db.session))
    admin.add_view(ModelView(Members_specie, db.session))
    admin.add_view(ModelView(Specie_filmography, db.session))
    admin.add_view(ModelView(Featuring_starship, db.session))
    admin.add_view(ModelView(Featuring_vehicle, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))