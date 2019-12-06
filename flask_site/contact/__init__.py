from flask import Blueprint

contact_us = Blueprint('contact_us', __name__)

from . import views

contact_us.add_url_rule('/', view_func=views.ContactPage.as_view('contact_us'))
contact_us.add_url_rule('/thank-you', view_func=views.ContactThankYouPage.as_view('thank_you'))
