from datetime import datetime
from flask_login import UserMixin

from flask_site import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    about_me = db.Column(db.String(10000))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    posts = db.relationship("Post", back_populates="user")

    def __repr__(self):
        return '{}'.format(self.username)
