from flask import render_template
from flask_login import login_required, current_user

from flask_site.users.models import User
from . import users
from ..blog.models import Post


@users.route('/profile')
@login_required
def user_profile():
    return render_template('users/user_profile.html', username=current_user.username)


@users.route('/<username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    user_posts = Post.query.filter_by(user_name=username)
    return render_template('users/user_posts.html', user=user, user_posts=user_posts)
