# email_sender/management/commands/submit_and_email.py
from django.core.management.base import BaseCommand
from email_sender.submit_form import submit_form
from email_sender.views import send_email
from django.test import RequestFactory

class Command(BaseCommand):
    help = 'Submit the Google form and send an email with the confirmation screenshot'

    def handle(self, *args, **kwargs):
        submit_form()
        factory = RequestFactory()
        request = factory.get('/send-email/')
        send_email(request)
