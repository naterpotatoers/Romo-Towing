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
    form = PriceEstimatorForm()
    price = 0.00

    chp_tow_fee = 244.00
    chp_outside_storage_fee = 59.00

    fpd_tow_fee = 229.00
    fpd_outside_storage_fee = 58.00

    outside_storage_fee = 65.00

    hourly_fow_fee = 270.00
    tow_fee = 291.00

    if form.validate_on_submit():
        if(form.chpTow.data):
            price += chp_tow_fee + chp_tow_fee
        if(form.fpdTow.data):
            price += fpd_tow_fee + fpd_outside_storage_fee
        if(form.onLot.data):
            price += outside_storage_fee
        price += form.towHours.data * hourly_fow_fee + tow_fee
        return render_template('form.html', title="Price Estimator", form=form, value=price) 
    return render_template('form.html', title="Price Estimator", form=form) 

@app.route('/VehicleEntry', methods=['GET', 'POST'])
def vehicleEntry():
    form = VehicleForm()
    if form.validate_on_submit():      
        vehicle = Vehicle(year=form.year.data, make=form.make.data, model=form.model.data, milage=form.milage.data, info=form.info.data)
        db.session.add(vehicle)
        db.session.commit()
        flash('Vehicle Submitted!')
        return redirect(url_for('vehicleEntry'))
    return render_template('form.html', title='Vehicles For Sale', form=form)


@app.route('/Contact')
def contact():
    return render_template('contact.html', title='Contact Us')