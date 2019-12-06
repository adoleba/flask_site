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
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        body = request.form['body']

        ctx.update({
            'contact': Contact.query.filter_by(id=1).first(),
            'name': name,
            'email': email,
            'subject': subject,
            'body': body
        })
        send_email(subject, str(name), [current_app.config['MAIL_USERNAME']], body, email, name)

        return redirect('thank-you')


def send_email(subject, sender, recipients, body, email, name):
    page = render_template('contact/email.html', body=body, email=email, name=name, subject=subject)
    msg = Message(subject, sender=name, recipients=recipients, html=page, reply_to=email)
    mail.send(msg)
