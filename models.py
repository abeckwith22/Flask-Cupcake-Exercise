"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, Float, ForeignKeyConstraint

DATABASE_URL = 'postgresql:///cupcake_db'

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

"""Models"""
class Cupcake(db.Model):

    __tablename__ = 'cupcakes'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(String, nullable=False)
    size = db.Column(String, nullable=False)
    rating = db.Column(Float, nullable=False)
    image = db.Column(String, nullable=False, default='https://tinyurl.com/demo-cupcake')

