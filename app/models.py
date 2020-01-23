from app import db, app

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(32), index=True, unique=False)
    make = db.Column(db.String(32), index=True, unique=False)
    model = db.Column(db.String(32), index=True, unique=False)
    vin = db.Column(db.String(32), index=True, unique=True)


    def __repr__(self):
        return self.vin