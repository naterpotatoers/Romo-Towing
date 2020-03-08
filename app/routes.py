from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import VehicleForm, PriceEstimatorForm
from app.models import Vehicle

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Pricing', methods=['GET', 'POST'])
def pricing():
    return render_template('pricing.html', title="Pricing") 

@app.route('/VehicleEntry', methods=['GET', 'POST'])
def vehicleEntry():
    forSale = Vehicle.query.all()
    form = VehicleForm()
    if form.validate_on_submit():      
        vehicle = Vehicle(year=form.year.data, make=form.make.data, model=form.model.data, milage=form.milage.data, info=form.info.data)
        db.session.add(vehicle)
        db.session.commit()
        flash('Vehicle Submitted!')
        return redirect(url_for('vehicleEntry'))
    return render_template('form.html', title='Vehicles For Sale', form=form, forSale = forSale)


@app.route('/Contact')
def contact():
    return render_template('contact.html', title='Contact Us')