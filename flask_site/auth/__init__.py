from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

auth.add_url_rule('/login', view_func=views.Login.as_view('login'))
