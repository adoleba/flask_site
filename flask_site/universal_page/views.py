from flask import render_template, request
from flask.views import MethodView, View

from flask_site.common.views import PageView
from flask_site.universal_page.models import UniversalPage


class SamplePage(PageView):

    def dispatch_request(self, *args, **kwargs):

        ctx = self.get_context_data(**kwargs)
        url = ctx['url']
        page = UniversalPage.query.filter_by(url=url).first()

        return render_template('universal_page/universal_page.html', page=page, **ctx)
