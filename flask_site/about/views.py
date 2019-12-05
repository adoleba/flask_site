from flask import render_template

from flask_site.about.models import About
from flask_site.main.views import PageView


class AboutPage(PageView):
    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'about': About.query.filter_by(id=1).first(),
        })
        return render_template('about/about.html', **ctx)
