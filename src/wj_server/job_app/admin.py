from django.contrib import admin

# Register your models here.
from .models import (
	JobProfile,
	RecruiterProfile
	)

admin.site.register(JobProfile)
admin.site.register(RecruiterProfile)