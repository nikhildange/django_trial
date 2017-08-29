from rest_framework import serializers
from .models import JobProfile, RecruiterProfile

class JobProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobProfile
		fields = ('job_title','job_type', 'job_status')

class RecruiterSerializer(serializers.ModelSerializer):
	class Meta:
		model = RecruiterProfile
		fields = ('name','email')