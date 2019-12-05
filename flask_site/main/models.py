from datetime import datetime

from flask_site import db


class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    title_description = db.Column(db.Text())
    about_intro = db.Column(db.String())
    about_description = db.Column(db.Text())
    first_card_title = db.Column(db.String())
    first_card_description = db.Column(db.Text())
    second_card_title = db.Column(db.String())
    second_card_description = db.Column(db.Text())
    third_card_title = db.Column(db.String())
    third_card_description = db.Column(db.Text())
    blog_intro = db.Column(db.String())
    blog_title = db.Column(db.Text())
    edited = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return self.title
