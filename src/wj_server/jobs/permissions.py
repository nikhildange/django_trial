from rest_framework.permissions import BasePermission
from employers.models import (
	Employer,
	)
from seekers.models import (
	Seeker,
	)

class IsEmployer(BasePermission):
	message = "You must be EMPLOYER."

	def has_permission(self, request, view): #required while creation
		print("has permission")
		if request.user.is_superuser:
			print("is spusr")
			return True
		else:
			if Employer.objects.filter(user=request.user).exists():
				print("exits")
				return True
			return False
		
	def has_object_permission(self, request, view, object):
		print("has obj permission")
		if request.user.is_superuser:
			print("is spusr")
			return True
		else:
			if Employer.objects.filter(user=request.user).exists():
				print("exists"+" "+str(object.employer.user.email)+" "+str(request.user.email))
				return object.employer.user == request.user
			print("out")
			return False


class IsSeeker(BasePermission):
	message = "You must be SEEKER."

	def has_permission(self, request, view): #required while creation
		print("has permission")
		if request.user.is_superuser:
			print("is spusr")
			return True
		else:
			if Seeker.objects.filter(user=request.user).exists():
				print("exits")
				return True
			return False
		
	def has_object_permission(self, request, view, object):
		if request.user.is_superuser:
			return True
		else:
			if Seeker.objects.filter(user=request.user).exists():
				return object.seeker.user == request.user
			return False