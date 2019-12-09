from flask import Blueprint

universal_page = Blueprint('universal_page', __name__)

from . import views

universal_page.add_url_rule('/<id>', view_func=views.SamplePage.as_view('render_page'))
