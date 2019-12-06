from flask import render_template, request, redirect

from flask_site.common.views import PageView
from flask_site.contact.forms import ContactForm
from flask_site.contact.models import Contact


class ContactPage(PageView):

    def get(self, **kwargs):
        form = ContactForm()
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'contact': Contact.query.filter_by(id=1).first(),
            'form': form
        })
        return render_template('contact/contact.html', **ctx)

    def post(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'contact': Contact.query.filter_by(id=1).first(),
            'name': request.form['name'],
            'email': request.form['email'],
            'subject': request.form['subject'],
            'body': request.form['body']
        })
