from django.core.mail import send_mail
from django.utils.timezone import now
from .models import FollowUp


def send_due_followups():
    today = now().date()
    followups = FollowUp.objects.filter(due_date=today)

    for f in followups:
        if f.email:
            send_mail(
                subject="Clinic Follow-up Reminder",
                message=(
                    f"Hello {f.patient_name},\n\n"
                    f"This is a reminder for your clinic follow-up today.\n\n"
                    f"Clinic: {f.clinic.name}\n"
                    f"Date: {f.due_date}\n\n"
                    "Thank you."
                ),
                from_email=None,
                recipient_list=[f.email],
                fail_silently=False,
            )
            print(f"Email sent to {f.email}")
