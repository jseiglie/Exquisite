"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Employee, Locales, Checks, Roles, Vacations, Incidents, Reports, Schedule, Month_Schedule, Shifts, Inventory, Categories, Sub_Categories, Deliveries, Meals, Ingredients, Daily_Menus, Clients, Orders, Tables, Reservations 

from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200