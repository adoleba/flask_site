from flask import render_template
from flask.views import MethodView

from . import main


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


@main.route('/')
def main():
    return render_template('index.html')
