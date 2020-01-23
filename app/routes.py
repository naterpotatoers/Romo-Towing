from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import VehicleForm
from app.models import Vehicle

@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Pricing', methods=['GET', 'POST'])
def pricing():
    form = VehicleForm()
    if form.validate_on_submit():
        vehicle = Vehicle(year=form.year.data, make=form.make.data, model=form.model.data, vin=form.vin.data)
        db.session.add(vehicle)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('pricing'))
    return render_template('pricing.html', form=form)
