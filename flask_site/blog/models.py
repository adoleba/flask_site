from datetime import datetime

from flask_site import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(200))
    body = db.Column(db.Text(), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_name = db.Column(db.Integer, db.ForeignKey('user.username'))
    user = db.relationship("User", back_populates="posts")

    def __repr__(self):
        return 'Post {}'.format(self.title)
