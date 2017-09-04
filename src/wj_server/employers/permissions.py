from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
	message = "You must be OWNER of this job post."
	def has_object_permission(self, request, view, object):
		return object.user == request.user
