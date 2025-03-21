from celery import shared_task
from django.template.loader import render_to_string
from lead.models import Lead
from django.core.mail import EmailMultiAlternatives, send_mail

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


@shared_task(name = 'week_tasks')
def lead_list(user):
    leads = Lead.objects.select_related('agent','agent__user','category').filter(organisation = user.profile, agent__isnull = False)
    subject = f"Count Lead"
    message = f"Number of leads currently credited per week { leads.count }"
    send_mail(subject, message, 'leadsystem@gmail.com', ['admin@gmail.com'])