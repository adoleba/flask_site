from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    about = db.Column(db.String(10000))
    created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '{}'.format(self.username)


admin = Admin(app)
admin.add_view(ModelView(User, db.session))


@app.route('/')
def main():
    return "hello world"


if __name__ == '__main__':
    app.run()
