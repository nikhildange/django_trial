from rest_framework import serializers
from .models import JobProfile

class JobProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = JobProfile
		fields = ('job_title','job_type')