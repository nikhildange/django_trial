from django.db.models import Q
from rest_framework.permissions import BasePermission
from seekers.models import (
	Seeker,
	)

class IsSeeker(BasePermission):
	message = "You must be SEEKER."
	def has_object_permission(self, request, view, object):
		if request.user.is_superuser:
			return True
		else:
			if Seeker.objects.filter(user=request.user).exists():
				return object.user == request.user
			return False
	