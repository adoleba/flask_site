from flask import render_template

from flask_login import login_required, current_user

from flask_site.blog.models import Post
from flask_site.universal_page.models import UniversalPage
from flask_site.users import users
from flask_site.users.models import Author


@users.route('/profile')
@login_required
def user_profile():
    pages = UniversalPage.query.all()
    return render_template('users/user_profile.html', username=current_user.username, pages=pages)


@users.route('/<username>')
def user_posts(username):
    author = Author.query.filter_by(username=username).first_or_404()
    author_posts = Post.query.filter_by(author_name=username)
    return render_template('users/user_posts.html', author=author, author_posts=author_posts)
