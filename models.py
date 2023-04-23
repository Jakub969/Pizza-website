from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazov = db.Column(db.String(50))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Rezervacia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meno = db.Column(db.String(100))
    priezvisko = db.Column(db.String(200))
    tel = db.Column(db.Integer)
    pocet = db.Column(db.Integer)
    mesto = db.Column(db.String(2))
    den = db.Column(db.Integer)
    mesiac = db.Column(db.Integer)
    rok = db.Column(db.Integer)
    hod = db.Column(db.Integer)
    min = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pizze = db.relationship('Pizza')
    rezervacie = db.relationship('Rezervacia')
