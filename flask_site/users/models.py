from datetime import datetime
from flask_login import UserMixin
from flask_security import RoleMixin

from flask_site import db


users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    description = db.Column(db.String(300))

    def __repr__(self):
        return self.name


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
    role = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '{}'.format(self.username)
