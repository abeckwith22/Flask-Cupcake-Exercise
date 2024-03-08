"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, redirect, flash, jsonify
from models import db, connect_db, Cupcake
import requests

def create_app():
    DATABASE_URL = 'postgresql:///cupcake_db'

    app = Flask(__name__)

    # app configs
    # app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False    # app configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SECRET_KEY'] = 'secret_key'
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['DEBUG'] = True

    connect_db(app)

    app.config['SQLALCHEMY_ECHO'] = True
    app.config['DEBUG'] = True

    return app

app = create_app()

"""Flask Routes"""

@app.route("/")
def display_homepage():
    return render_template('home.html')

@app.route("/api/cupcakes")
def get_cupcakes():
    """Gathers all cupcakes from db, displays them as JSON"""
    cupcakes = Cupcake.query.all()
    cupcake_serialized_list = [cupcake.serialize() for cupcake in cupcakes]
    return jsonify(cupcake_serialized_list)

@app.route("/api/cupcakes/<int:cupcake_id>")
def get_specific_cupcake(cupcake_id):
    cupcake = Cupcake.query.get(cupcake_id)
    serialized = cupcake.serialize()
    """Gets specific cupcake data from db using id, displays JSON"""
    return jsonify(cupcake=serialized)

@app.route("/api/cupcakes", methods=['POST'])
def add_cupcake():
    """Create cupcake from form data and return it."""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor, rating=rating, size=size, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    # We should return a status code 201 for returned
    return ( jsonify(serialized), 201 )

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """updates cupcake from db"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Removes cupcake from db"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")


""" Function Methods """

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
