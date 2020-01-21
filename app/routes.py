from app import app, db
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html')