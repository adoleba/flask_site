from flask import render_template

from flask_site.common.views import PageView
from flask_site.contact.forms import ContactForm
from flask_site.contact.models import Contact


class ContactPage(PageView):

    def get(self, **kwargs):
        form = ContactForm()
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'contact': Contact.query.filter_by(id=1).first(),
        })
        return render_template('contact/contact.html', **ctx)
