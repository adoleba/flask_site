from flask import render_template

from flask_site.common.views import PageView
from flask_site.universal_page.models import UniversalPage


class SamplePage(PageView):
    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'pages': UniversalPage.query.all(),
        })
        return render_template('universal_page/universal_page.html', **ctx)
