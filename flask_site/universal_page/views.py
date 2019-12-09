from flask import render_template, request

from flask_site.common.views import PageView
from flask_site.universal_page.models import UniversalPage


class SamplePage(PageView):
    def get(self, id, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'page': UniversalPage.query.get_or_404(id)
        })
        return render_template('universal_page/universal_page.html',  **ctx)
