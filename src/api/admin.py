  
import os
from flask_admin import Admin
from .models import db, Employee, Locales, Checks, Roles, Vacations, Incidents, Reports, Schedule, Month_Schedule, Shifts, Inventory, Categories, Sub_Categories, Deliveries, Meals, Ingredients, Daily_Menus, Clients, Orders, Tables, Reservations 
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Employee, db.session))
    admin.add_view(ModelView(Locales, db.session))
    admin.add_view(ModelView(Checks, db.session))
    admin.add_view(ModelView(Roles, db.session))
    admin.add_view(ModelView(Vacations, db.session))
    admin.add_view(ModelView(Incidents, db.session))
    admin.add_view(ModelView(Reports, db.session))
    admin.add_view(ModelView(Schedule, db.session))
    admin.add_view(ModelView(Month_Schedule, db.session))
    admin.add_view(ModelView(Shifts, db.session))
    admin.add_view(ModelView(Inventory, db.session))
    admin.add_view(ModelView(Categories, db.session))
    admin.add_view(ModelView(Sub_Categories, db.session))
    admin.add_view(ModelView(Deliveries, db.session))
    admin.add_view(ModelView(Meals, db.session))
    admin.add_view(ModelView(Ingredients, db.session))
    admin.add_view(ModelView(Daily_Menus, db.session))
    admin.add_view(ModelView(Clients, db.session))
    admin.add_view(ModelView(Orders, db.session))
    admin.add_view(ModelView(Tables, db.session))
    admin.add_view(ModelView(Reservations, db.session))
    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))