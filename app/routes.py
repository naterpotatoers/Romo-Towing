from app import app, db
from flask import render_template, flash, redirect, url_for


@app.route('/')
def hello_world():
    return 'Hello, World!'