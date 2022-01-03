from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRETE_KEY'] = 'dGVzdGluZwo='
# app.config['SQLALCHEMY_DATABASE_URI'] = ':memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


class User(db.Model):
    """[summary]

    Args:
        db ([type]): [description]
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
