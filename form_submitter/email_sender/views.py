# from django.shortcuts import render

# Create your views here.
# email_sender/views.py
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings
import os

def send_email(request):

    subject = 'Python (Selenium) Assignment - Vaibhav Rawat'
    message = (
        'Dear Hiring Team,\n\n'
        'I hope this email finds you well.\n\n'
        'I would like to extend my sincere apologies for the delay in submitting my Python (Selenium) assignment. '
        'Due to unforeseen circumstances, I encountered some difficulties that required additional time to resolve.\n\n'
        'Nevertheless, I am pleased to inform you that I have successfully completed the assignment. '
        'Please find the attached screenshot for confirmation.\n\n'
        'GitHub Repository: https://github.com/Rawat107/From-Auto-Mailer.git\n'
        'Resume: https://drive.google.com/file/d/1Op1voY7rZXEzsuUvSLZA_glotHJTzKs6/view?usp=drive_link\n\n'
        'Thank you for your understanding and patience.\n\n'
        'Best regards,\n'
        'Vaibhav Rawat'
    )

    email = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ['tech@themedius.ai'],  
        cc=['HR@themedius.ai']   
    )
    ss_path = "C:\\Users\\vaibh\\OneDrive\\Desktop\\From-Auto-Mailer\\form_submitter\\confirmation.png"
    if os.path.exists(ss_path):
        email.attach_file(ss_path)
    else:
        return HttpResponse('Test file does not exist')
    email.send()
    return HttpResponse('Email sent successfully')
