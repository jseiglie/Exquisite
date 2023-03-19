from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

#### HR
class Employee(db.Model):
    __tablename__ = "employee"
    id= db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    sex = db.Column(db.String(8), nullable=False)
    dni = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    province = db.Column(db.String(20), nullable=False)
    brut_salary = db.Column(db.Integer, nullable=False)
    irpf = db.Column(db.Integer, nullable=False)
    payments = db.Column(db.Integer, nullable=False)
    vacations_amount = db.Column(db.Integer, nullable=False)
    hired = db.Column(db.Date, nullable=False)
    fired = db.Column(db.Date, nullable=False)
    local = db.Column(db.Integer)
    role = db.Column(db.Integer)
    schedule = db.Column(db.Integer)
    reports = db.Column(db.Integer)
    incidents = db.Column(db.Integer)
    vacations = db.Column(db.Integer)
    check_in_out = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.full_name}"
    
    def serialize(self):
        return{
            "id": self.id,
            "full_name": self.full_name,
            "sex": self.sex,
            "dni": self.dni,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "city": self.city,
            "province": self.province,
            "brut_salary": self.brut_salary,
            "irpf": self.irpf,
            "payments": self.payments,
            "vacations_amount": self.vacations_amount,
            "hired": self.hired,
            "fired": self.fired,
            "local": self.local,
            "role": self.role,
            "schedule": self.schedule,
            "reports": self.reports,
            "incidents": self.incidents,
            "vacations": self.vacations,
            "check_in_out": self.check_in_out
        }

class Locales(db.Model):
    __tablename__ = "locales"
    id = db.Column(db.Integer, primary_key=True)
    local = db.Column(db.String(30))
    address = db.Column(db.String(100))

    def __repr__(self):
        return f"{locale}"
    def serialize(self):
        return {
        "id": self.id,
        "local": self.local,
        "address": self.address
        }

class Checks(db.Model):
    __tablename__ = "checks"
    id = db.Column(db.Integer, primary_key=True)
    check_in = db.Column(db.String(80))
    check_out = db.Column(db.String(80))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Checks {self.id}" 
    
    def serialize(self):
        return{
            "id": self.id,
            "check_in": self.check_in,
            "check_out": self.check_out,
            "date": self.date
        }

class Roles(db.Model):
    __tablename__ ="roles"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10))

    def __repr__(self):
        return f"{self.role}"
    def serialize(self):
        return{
        "id": self.id,
        "role": self.role
        }

class Vacations(db.Model):
    __tablename__ = "vacations"
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.DateTime, nullable=False)
    end= db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Vacations {self.id}"
    def serialize(self):
        return{
            "id": self.id,
            "start": self.start,
            "end": self.end
        }

class Incidents(db.Model):
    __tablename__ = "incidents"
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(5), nullable=False)
    incident = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Incident {self.id}"
    def serialize(self):
        return{
            "id": self.id,
            "level": self.level,
            "incident": self.incident,
            "date": self.date
        }

class Reports(db.Model):
    __tablename__ = "reports"
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(5), nullable=False)
    report = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Report {self.id}"
    def serialize(self):
        return{
            "id": self.id,
            "level": self.level,
            "report": self.incident,
            "date": self.date
        }

class Schedule(db.Model):
    __tablename__ = "schedule"
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(500), nullable=False)
    year = db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return f"Schedule {self.id}"
    def serialize(self):
        return{
            "id": self.id,
            "month": self.month,
            "year": self.year,
        }

class Month_Schedule(db.Model):
    __tablename__ = "month_schedule"
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer)

    def __repr__(self):
        return f"Month Schedule {self.id}"
    
    def serialize(self):
        return{
            "id": self.id,
            "month": self.month
        }
class Shifts(db.Model):
    __tablename__ = "shifts"
    id = db.Column(db.Integer, primary_key=True)
    shift = db.Column(db.String(20), nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end= db.Column(db.DateTime, nullable=False)
    def __repr__(self):
        return f"{self.shift}"
    def serialize(self):
        return{
            "id": self.id,
            "shift": self.shift,
            "start": self.start,
            "end": self.end
        }

## Inventory

categories_rel = db.Table("categories_rel", 
db.Column("inventory_id", db.Integer, db.ForeignKey("inventory.id"), primary_key=True),
db.Column("categories_id", db.Integer, db.ForeignKey("categories.id"), primary_key=True)
)

sub_categories_rel = db.Table("sub_categories_rel", 
db.Column("inventory_id", db.Integer, db.ForeignKey("inventory.id"), primary_key=True),
db.Column("sub_categories_id", db.Integer, db.ForeignKey("sub_categories.id"), primary_key=True)
)


class Inventory(db.Model):
    __tablename__ = "inventory"
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False) 
    category = db.relationship("Categories", secondary=categories_rel, lazy="subquery", backref=db.backref("category_rel", lazy=True))
    sub_category = db.relationship("Sub_Categories", secondary=sub_categories_rel, lazy="subquery", backref=db.backref("sub_category_rel", lazy=True))
    last_deliver = db.Column(db.Integer, db.ForeignKey("deliveries.id"))

    def __repr__(self):
        return{f"{self.item}"}
    def serialize(self):
        return {
            "id": self.id,
            "item": self.item,
            "quantity": self.quantity,
            "category": self.category,
            "sub_category": self.sub_category,
            "last_deliver": self.last_deliver
        }
class Categories(db.Model):
    __tablename__ ="categories"
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(20), nullable=False)
    

    def __repr__(self):
        return f"{self.category}"
    def serialize(self):
        return {
            "id": self.id,
            "category": self.category
        }
    
class Sub_Categories(db.Model):
    __tablename__ = "sub_categories"
    id = db.Column(db.Integer, primary_key=True)
    sub_category = db.Column(db.String(20))

    def __repr__(self):
        return f"{self.sub_category}"
    def serialize(self):
        return {
            "id": self.id,
            "sub_category": self.sub_category
        }
    
class Deliveries(db.Model):
    __tablename__ = "deliveries"
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(40), nullable=False)
    order = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f"Deliveries {self.id}"
    def serialize(self):
        return {
            "id": self.id,
            "company": self.company,
            "order": self.order,
            "date": self.date
        }

class Meals(db.Model):
    __tablename__ ="meals"
    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Integer)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.meal}"
    def serialize(self):
        return{
            "id": self.id,
            "meal": self.meal,
            "ingredients" : self.ingredients,
            "price": self.price
        }

class Ingredients(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True)
    ingredient = db.Column(db.String(100), nullable=False)
    cuantity = db.Column(db.Integer, nullable=False)
    availeable = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self):
        return f"{self.ingredient}"
    def serialize(self):
        return{
        "id": self.id,
        "ingredient": self.ingredient,
        "cuantity": self.cuantity,
        "availeable": self.availeable
        }
class Daily_Menus(db.Model):
    __tablename__ ="daily_menus"
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.Integer)
    second = db.Column(db.Integer)
    third= db.Column(db.Integer)
    price= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Daily_Menus {self.id}"
    def serialize(self):
        return{
        "id": self.id,
        "first": self.first,
        "second": self.second,
        "third": self.third,
        "price": self.price
        }

class Clients(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    contact = db.Column(db.String(40), nullable=False)
    table = db.Column(db.Integer)
    order = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.name}"
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "contact": self.contact,
            "table": self.table,
            "order": self.order
        }

class Orders(db.Model):
    __tablename__ ="orders"
    id = db.Column(db.Integer, primary_key=True)
    ordered = db.Column(db.Integer)
    total = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    table = db.Column(db.Integer)
    client = db.Column(db.Integer)

    def __repr__(self):
        return f"Orders {self.id}"
    def serialize(self):
        return {
            "id": self.id,
            "ordered": self.ordered,
            "total": self.total,
            "date": self.date,
            "table": self.table,
            "client": self.client
        }

class Tables(db.Model):
    __tablename__ = "tables"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    client = db.Column(db.Integer)
    order = db.Column(db.Integer)
    diners = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Table {self.number}"
    def serialize(self):
        return{
            "id": self.id,
            "number": self.number,
            "hour": self.hour,
            "date": self.date,
            "client": self.client,
            "order": self.order,
            "diners": self.diners
        }

class Reservations(db.Model):
    __tablename__ ="reservations"
    id = db.Column(db.Integer, primary_key=True)
    table = db.Column(db.Integer)
    client = db.Column(db.Integer)
    time = db.Column(db.DateTime, nullable=False)
    diners = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Reservation {self.id}"
    def serialize(self):
        return {
            "id": self.id,
            "table": self.table,
            "client": self.client,
            "diners": self.diners,
            "time": self.time
        }
