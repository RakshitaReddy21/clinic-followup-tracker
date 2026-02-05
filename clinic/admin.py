from django.contrib import admin
from .models import Clinic, FollowUp, UserProfile

admin.site.register(Clinic)
admin.site.register(FollowUp)
admin.site.register(UserProfile)


