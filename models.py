from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
    
class Admin(db.Model):
    username = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String(50), nullable = False)

class User(db.Model):
    username = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String(50), nullable = False)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    
class User_cart(db.Model):
    entry_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    username = db.Column(db.String(50), nullable = False)
    pid = db.Column(db.Integer, nullable = False)
    pname = db.Column(db.String(50), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    unit_cost = db.Column(db.Integer)  
    cost = db.Column(db.Integer, nullable = False)
    category = db.Column(db.String(50), nullable = False)
    image_url = db.Column(db.String(100), nullable = False)
    
class Products(db.Model):
    pid = db.Column(db.Integer, primary_key = True)
    pname = db.Column(db.String(50), nullable = False)
    pprice = db.Column(db.Integer, nullable = False)
    pcount = db.Column(db.Integer, nullable = False)
    image_url = db.Column(db.String(100), nullable = False)
    category = db.Column(db.String(50), nullable = False)

class Categories(db.Model):
    cname = db.Column(db.String(50), primary_key = True)