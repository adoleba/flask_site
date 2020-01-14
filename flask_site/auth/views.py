from flask_mail import Message

from flask_site.auth import auth

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from flask_site.auth.forms import SignupForm, LoginForm, ForgotForm, PasswordResetForm
from flask_site.users.models import User
from flask_site import db, mail
from flask_site.universal_page.models import UniversalPage
import uuid


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    pages = UniversalPage.query.all()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('users.user_profile'))

    return render_template("auth/login.html", form=form, pages=pages)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    pages = UniversalPage.query.all()
    return render_template("auth/logout.html", pages=pages)


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    pages = UniversalPage.query.all()

    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        user_verify_email = User.query.filter_by(email=email).first()
        if user_verify_email:
            flash('Email address already exists.')

        user_verify_username = User.query.filter_by(username=username).first()
        if user_verify_username:
            flash('Username already exists.')

        if request.form['password'] != request.form['password2']:
            flash('Passwords are not the same.')

        if form.validate_on_submit():
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.registered'))

    return render_template('auth/signup.html', form=form, pages=pages)


@auth.route('/registered')
def registered():
    pages = UniversalPage.query.all()
    return render_template('auth/registered.html', pages=pages)


@auth.route('/forgot', methods=["GET", "POST"])
def forgot_password():
    pages = UniversalPage.query.all()
    form = ForgotForm()

    if form.validate_on_submit():
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            code = str(uuid.uuid4())
            user.change_configuration = {
                "password_reset_code": code
            }
            user.password_code = code
            db.session.commit()
            send_email(user)

        flash('You will receive a password reset email if we find email in our system')
    return render_template("auth/forgot_password.html", form=form, pages=pages)


@auth.route('/password_reset/<username>/<code>', methods=["GET", "POST"])
def reset_password(username, code):
    pages = UniversalPage.query.all()
    user = User.query.filter_by(username=username).first()
    form = PasswordResetForm()

    if code == user.password_code:

        if request.method == 'POST':
            password = request.form['password']

            if request.form['password'] != request.form['password2']:
                flash('Passwords are not the same.')
                password_compliance = False
            else:
                password_compliance = True

            if password_compliance:
                if form.validate_on_submit():
                    user.password = generate_password_hash(password, method='sha256')
                    user.password_code = ''
                    db.session.commit()
                    flash('Your password was changed. You can log in')

        return render_template("auth/reset_password.html", form=form, user=user)

    return render_template("auth/invalid_password_code.html", form=form, user=user, pages=pages)


def send_email(user):
    page = render_template('auth/reset_password_email.html', user=user)
    msg = Message(recipients=[user.email], html=page, sender='Flask Blog', subject='Reset Password')
    mail.send(msg)
