from flask import Blueprint

about_us = Blueprint('about_us', __name__)

from . import views

about_us.add_url_rule('/', view_func=views.AboutPage.as_view('about_us'))
