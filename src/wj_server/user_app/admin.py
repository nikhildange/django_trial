from django.contrib import admin

# Register your models here.
from .models import UserProfile, JobApplied

admin.site.register(UserProfile)
admin.site.register(JobApplied)