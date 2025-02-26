from celery import shared_task
from django.template.loader import render_to_string
from lead.models import Lead
from django.core.mail import EmailMultiAlternatives

@shared_task
def send_lead_message(lead_id):
    lead  = Lead.objects.get(id = lead_id)
    subject = f"Message from the company"
    message = f"The company informs you that you have been added to the queue at number { lead.id}"
    html_message = render_to_string('lead/include/emailsend.html', {"lead":lead})
    mail = EmailMultiAlternatives(subject, message, 'admin@gmail.com', [lead.email])
    mail.attach_alternative(html_message, 'text/html')
    mail.send()
    return f"Email was sender!"
    