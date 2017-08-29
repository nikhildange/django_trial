from rest_framework import serializers
from .models import UserProfile, JobApplied

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ('name', 'email', 'display_lang', 'address', 'user_status')


class UserJobSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobApplied
		fields = ('user_profile_id', 'job_profile_id', 'job_applied_status')