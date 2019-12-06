from flask import render_template, request, redirect, current_app
from flask_mail import Message

from flask_site import mail
from flask_site.common.views import PageView
from flask_site.contact.forms import ContactForm
from flask_site.contact.models import Contact, ContactThankYou


class ContactThankYouPage(PageView):

    def get(self, **kwargs):
        ctx = self.get_context_data(**kwargs)
        ctx.update({
            'contact': ContactThankYou.query.filter_by(id=1).first(),
        })
        return render_template('contact/contact_thank_you.html', **ctx)


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
        send_email(current_app.config['MAIL_USERNAME'], **ctx)

        return redirect('thank-you')


def send_email(recipients, **ctx):
    page = render_template('contact/email.html', **ctx)
    msg = Message(ctx['subject'], sender=ctx['name'], recipients=[recipients], html=page, reply_to=ctx['email'])
    mail.send(msg)
