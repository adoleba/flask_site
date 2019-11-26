from flask import render_template, redirect, url_for

from flask_site import db
from flask_site.auth.forms import SignupForm
from flask_site.users.models import User
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    return render_template('auth/logout.html')


@auth.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User()
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)
