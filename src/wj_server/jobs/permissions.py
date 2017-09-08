from rest_framework.permissions import BasePermission
from employers.models import (
	Employer,
	)
from seekers.models import (
	Seeker,
	)

class IsEmployer(BasePermission):
	message = "You must be EMPLOYER."
	def has_object_permission(self, request, view, object):
		if request.user.is_superuser:
			return True
		else:
			if Employer.objects.filter(user=request.user).exists():
				return object.employer == request.user
			return False

class IsOwner(BasePermission):
	message = "You must be OWNER of this JOB."
	def has_object_permission(self, request, view, object):
		if request.user.is_superuser:
			return True
		else:
			return object.employer == request.user

class IsSeeker(BasePermission):
	message = "You must be SEEKER."
	def has_object_permission(self, request, view, object):
		if request.user.is_superuser:
			return True
		else:
			if Seeker.objects.filter(user=request.user).exists():
				return object.user == request.user
			else:
				return False