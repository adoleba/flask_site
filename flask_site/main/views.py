from flask import render_template

from .models import Home
from flask_site.common.views import PageView


class HomePage(PageView):
    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'home': Home.query.filter_by(id=1).first(),
        })
        return render_template('index.html', **ctx)
