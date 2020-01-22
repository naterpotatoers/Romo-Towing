from app import app, db
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/Home')
def home():
    return render_template('home.html')

@app.route('/Pricing')
def pricing():
    return render_template('pricing.html')