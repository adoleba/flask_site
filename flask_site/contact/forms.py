from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    name = StringField('Your Name: ', validators=[DataRequired()])
    email = StringField('Your email: ', validators=[DataRequired()])
    subject = StringField('Subject: ', validators=[DataRequired()])
    body = StringField('Your message: ', validators=[DataRequired()])
    submit = SubmitField('Send')
