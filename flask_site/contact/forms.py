from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Your Name: ', validators=[DataRequired()])
    email = StringField('Your email: ', validators=[DataRequired()])
    subject = StringField('Subject: ', validators=[DataRequired()])
    body = TextAreaField('Your message: ', validators=[DataRequired()])
    submit = SubmitField('Send')
