from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from leads.models import Lead


@shared_task
def process_new_lead(lead_id):

    lead = Lead.objects.get(id=lead_id)

    send_customer_email(lead)

    send_internal_notification(lead)

    return True


def send_customer_email(lead):

    subject = "Thank you for your inquiry"

    html_content = render_to_string(
        "emails/customer_confirmation.html",
        {
            "name": lead.name
        }
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        body="Thank you for your inquiry",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[lead.email]
    )

    msg.attach_alternative(html_content, "text/html")

    msg.send()


def send_internal_notification(lead):

    subject = "New Lead Received"

    html_content = render_to_string(
        "emails/internal_notification.html",
        {
            "name": lead.name,
            "email": lead.email,
            "phone": lead.phone,
            "source": lead.source,
            "campaign": lead.campaign
        }
    )

    msg = EmailMultiAlternatives(
        subject=subject,
        body="New lead received",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["bhutadaaditya08@gmail.com"]
    )

    msg.attach_alternative(html_content, "text/html")

    msg.send()


# from celery import shared_task
# # from .models import Lead
# import time
# from leads.models import Lead

# @shared_task
# def process_new_lead(lead_id):

#     try:

#         lead = Lead.objects.get(id=lead_id)

#         # Simulate processing (e.g., sending to CRM, enrichment, etc.)
#         # For demonstration, we'll just mark it as processed after a delay

#         # import time
#         print(f"********* Processing lead: {lead_id}")
#         time.sleep(5)  # Simulate time-consuming processing
#         print(f"Finished processing lead: {lead_id} *********")
#         lead.status = 'processed'

#         lead.save()

#     except Lead.DoesNotExist:

#         pass

