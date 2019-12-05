from datetime import datetime

from flask_site import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    sub_title = db.Column(db.Text())
    body = db.Column(db.Text())
    edited = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return self.title
