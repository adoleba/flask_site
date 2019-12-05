from flask.views import MethodView


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