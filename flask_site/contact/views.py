from flask import render_template

from flask_site.common.views import PageView


class ContactPage(PageView):
    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        return render_template('contact/contact.html', **ctx)
