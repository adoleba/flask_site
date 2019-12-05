from datetime import datetime

from flask_site import db


class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    title_description = db.Column(db.Text())
    red_intro = db.Column(db.String())
    black_intro = db.Column(db.String())
    intro_description = db.Column(db.Text())
    first_offer = db.Column(db.String())
    first_offer_description = db.Column(db.Text())
    second_offer = db.Column(db.String())
    second_offer_description = db.Column(db.Text())
    third_offer = db.Column(db.String())
    third_offer_description = db.Column(db.Text())
    first_step = db.Column(db.String())
    first_step_description = db.Column(db.Text())
    second_step = db.Column(db.String())
    second_step_description = db.Column(db.Text())
    third_step = db.Column(db.String())
    third_step_description = db.Column(db.Text())
    edited = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return self.title
