from flask import render_template

from . import users


@users.route('/profile')
def user_profile():
    return render_template('users/user_profile.html')
