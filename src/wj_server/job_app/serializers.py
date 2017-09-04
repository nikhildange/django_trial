from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	)
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


class JobProfileListSerializer(ModelSerializer):
	# url = HyperlinkedIdentityField(
	# 	view_name = 'jobs:read',
	# 	lookup_field = 'pk'
	# 	)
	recruiter = SerializerMethodField()
	# url = job_detail_url
	class Meta:
		model = JobProfile
		fields = ['id', 'job_title', 'job_type', 'job_status', 'recruiter']
	def get_recruiter(self, obj):
		return str(obj.recruiter.user.email)


class JobProfileSerializer(ModelSerializer):
	recruiter = SerializerMethodField()
	class Meta:
		model = JobProfile
		fields = ('id', 'job_title', 'job_type', 'job_status', 'recruiter')
	def get_recruiter(self, obj):
		return str(obj.recruiter.user.email)


class RecruiterSerializer(ModelSerializer):
	class Meta:
		model = RecruiterProfile
		fields = ('id', 'name', 'email')
