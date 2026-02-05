# clinic/models.py
import secrets
from django.db import models
from django.contrib.auth.models import User


def generate_clinic_code():
    return secrets.token_hex(4)


def generate_public_token():
    return secrets.token_urlsafe(16)


class Clinic(models.Model):
    name = models.CharField(max_length=255)
    clinic_code = models.CharField(
        max_length=12,
        unique=True,
        default=generate_clinic_code
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(
    Clinic,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)


    def __str__(self):
        return self.user.username


class FollowUp(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]

    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    patient_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    language = models.CharField(
        max_length=2,
        choices=[('en', 'English'), ('hi', 'Hindi')],
        default='en'
    )
    notes = models.TextField(blank=True)

    due_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    public_token = models.CharField(
        max_length=64,
        unique=True,
        default=generate_public_token
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_name


class PublicViewLog(models.Model):
    followup = models.ForeignKey(FollowUp, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

