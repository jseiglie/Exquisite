"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Employee, Locales, Checks, Roles, Vacations, Incidents, Reports, Schedule, Month_Schedule, Shifts, Inventory, Categories, Sub_Categories, Deliveries, Meals, Ingredients, Daily_Menus, Clients, Orders, Tables, Reservations 
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200

@api.route("/login", methods=["POST"])
def login():
    data = request.json
    user = Employee.query.filter_by(email = data['email'], password = data['password']).one_or_none()
    if not user:
        return jsonify({"error": "Correo o contraseña incorrecta"}), 400
    access_token = create_access_token(identity=user.id)
    return jsonify({"token": access_token, "employee": user.serialize()}), 200

@api.route("/getEmployee", methods=["GET"])
def getEmployee():
    employees = Employee.query.all()
    data = [employee.serialize() for employee in employees]
    return jsonify(data), 200 

@api.route("/employee_details/<int:id>", methods=["GET"])
def employeeDetails(id):
    query = Employee.query.get(id)
    schedule = Schedule.query.filter_by(employee_id = id)
    print(query) 
    return jsonify(query.serialize(), schedule.serialize()), 200

@api.route("/employee_edit/<int:id>", methods=["PUT"])
def employee_edit(id):
    return({"msg": "asd"}),200



@api.route("/shift", methods=["GET"])
def getShift():
    query = Shifts.query.all()
    data = [shift.serialize() for shift in query]
    return jsonify(data)  