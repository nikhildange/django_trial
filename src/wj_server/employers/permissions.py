from django.db.models import Q
from rest_framework.permissions import BasePermission
from employers.models import (
	Employer,
	)

class IsEmployer(BasePermission):
	message = "You must be EMPLOYER."
	def has_object_permission(self, request, view, object):
		if request.user.is_superuser:
			return True
		else:
			if Employer.objects.filter(user=request.user).exists():
				return object.user == request.user
			return False