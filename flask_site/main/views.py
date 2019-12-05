from flask import render_template
from flask.views import MethodView

from . import main
from .models import Home


class ContextMixin:
    extra_context = None

    def get_context_data(self, **kwargs):
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs


class PageView(ContextMixin, MethodView):

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return ctx


class HomePage(PageView):
    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'home': Home.query.filter_by(id=1).first(),
        })
        return render_template('index.html', **ctx)
