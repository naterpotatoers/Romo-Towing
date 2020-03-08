from app import db, app
from datetime import datetime
from time import time

condition = ["Perfect", "Good", "Decent", "Poor"]

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, index=True, unique=False)
    make = db.Column(db.String(32), index=True, unique=False)
    model = db.Column(db.String(32), index=True, unique=False)
    milage = db.Column(db.String(32), index=True, unique=False)
    info = db.Column(db.String(500), index=True, unique=False)

    def __repr__(self):
        return '<For Sale: {} {} {} {}>'.format(self.year, self.make, self.model, self.milage)

