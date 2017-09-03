from rest_framework.serializers import ModelSerializer
from .models import (
	JobProfile,
	RecruiterProfile
)

class JobProfileCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = JobProfile
		fields = ('job_type', 'job_title', 
			'job_status', 'opening_count', 'recruiter', 'address', 
			'hour_wage_low', 'hour_wage_high', 'id')

class JobProfileSerializer(ModelSerializer):
	class Meta:
		model = JobProfile
		fields = ('id', 'job_title', 'job_type', 'job_status')


class RecruiterSerializer(ModelSerializer):
	class Meta:
		model = RecruiterProfile
		fields = ('id', 'name', 'email')
