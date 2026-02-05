def send_followup_reminder(followup):
    """
    Notification entry point.
    In production, this can be extended to support SMS providers.
    """
    print(
        f"Reminder sent to {followup.patient_name} "
        f"({followup.phone}) for {followup.due_date}"
    )

