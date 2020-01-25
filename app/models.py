from app import db, app
from datetime import datetime
from time import time

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, index=True, unique=False)
    make = db.Column(db.String(32), index=True, unique=False)
    model = db.Column(db.String(32), index=True, unique=False)
    vin = db.Column(db.String(32), index=True, unique=True)
    arrivalDate = db.Column(db.DateTime, index=True, unique=False)


    def __repr__(self):
        return '<Vehicle VIN: {}>'.format(self.vin)
        


