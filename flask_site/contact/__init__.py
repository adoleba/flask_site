from flask import Blueprint

contact = Blueprint('contact', __name__)

from . import views

contact.add_url_rule('/', view_func=views.ContactPage.as_view('contact'))
