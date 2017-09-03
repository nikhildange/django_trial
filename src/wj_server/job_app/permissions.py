from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
	message = "You must be recruiter of this job post"
	def has_object_permission(self, request, view, obj):
		return obj.recruiter == request.user
		# member = MemberShip.objects.get(user=request.user)
		# member.is_active
		# safe_method = ['PUT'] // self.safe_method
		# if request.method in SAFE_METHODS
		