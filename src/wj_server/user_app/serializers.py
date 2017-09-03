from rest_framework.serializers import ModelSerializer
from .models import (
	JobApplied,
	UserProfile
	)

class UserProfileSerializer(ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('id', 'name', 'email', 'display_lang', 'address', 'user_status')


class UserJobSerializer(ModelSerializer):
	class Meta:
		model = JobApplied
		fields = ('id', 'user_profile_id', 'job_profile_id', 'job_applied_status')