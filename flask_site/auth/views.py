from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from flask_site.auth.forms import SignupForm, LoginForm
from flask_site.users.models import User
from . import auth
from .. import db


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))

        login_user(user)
        return redirect(url_for('users.user_profile'))

    return render_template("auth/login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template("auth/logout.html")


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        user_verify_email = User.query.filter_by(email=email).first()
        if user_verify_email:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        user_verify_username = User.query.filter_by(username=username).first()
        if user_verify_username:
            flash('Username already exists')
            return redirect(url_for('auth.signup'))

        if form.validate_on_submit():
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.registered'))

    return render_template('auth/signup.html', form=form)


@auth.route('/registered')
def registered():
    return render_template('auth/registered.html')


