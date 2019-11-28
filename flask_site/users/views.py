from flask import render_template
from flask_login import login_required, current_user

from . import users


@users.route('/profile')
@login_required
def user_profile():
    return render_template('users/user_profile.html', username=current_user.username)
