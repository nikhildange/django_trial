from django.contrib import admin
from .models import (
	Application,
	Job,
	)
admin.site.register(Application)
admin.site.register(Job)