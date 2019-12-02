from flask import Blueprint

blog = Blueprint('blog', __name__)

from . import views

blog.add_url_rule('/', view_func=views.BlogPage.as_view('blog_page'))
