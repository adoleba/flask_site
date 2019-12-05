from flask import Blueprint

main = Blueprint('main', __name__)

from . import views

main.add_url_rule('/', view_func=views.HomePage.as_view('main'))
