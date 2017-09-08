from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	message = "You must be OWNER of this JOB."
	def has_object_permission(self, request, view, object):
		if request.user.is_superuser:
			return True
		else:
			return object.employer == request.user
