from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

auth.add_url_rule('/login', view_func=views.Login.as_view('login'))
auth.add_url_rule('/logout', view_func=views.Logout.as_view('logout'))
auth.add_url_rule('/register', view_func=views.Register.as_view('register'))
auth.add_url_rule('/registered', view_func=views.RegisteredView.as_view('registered'))
