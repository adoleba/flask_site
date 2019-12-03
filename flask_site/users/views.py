from flask import render_template
from flask_login import login_required, current_user

from flask_site.users.models import User
from . import users


@users.route('/profile')
@login_required
def user_profile():
    return render_template('users/user_profile.html', username=current_user.username)


@users.route('/<username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('users/user_posts.html', user=user)
