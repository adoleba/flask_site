from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3, 80), Regexp('^[A-Za-z0-9_]{3,}$',
        message='Usernames consist of numbers, letters and underscores')])
    password = PasswordField('Password', validators=[DataRequired(),
        EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 120), Email()])


class LoginForm(FlaskForm):
    username = StringField('Your Username: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class ForgotForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])


class PasswordResetForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password2')])
