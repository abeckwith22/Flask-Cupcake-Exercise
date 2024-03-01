"""Flask app for Cupcakes"""
from flask import Flask, render_template, redirect, flash
from models import connect_db, Cupcake 
import requests

def create_app():
    DATABASE_URL = 'postgresql:///cupcake_db'

    app = Flask(__name__)

    # app configs
    # app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = Fals    # app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['DEBUG'] = True

    connect_db(app)

    return appe
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['DEBUG'] = True

    connect_db(app)

    return app

app = create_app()

@app.route("/")
def show_homepage():
    return render_template('home.html')

@app.route("/api/cupcakes")
def show_homepage():
    return render_template('home.html')

@app.route("/api/cupcakes/<int:cupcake_id>")
def show_homepage(cupcake_id):
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)