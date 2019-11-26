from flask import render_template

from . import users


@users.route('/profile/<username>')
def user_profile(username):
    return render_template('users/user_profile.html')
