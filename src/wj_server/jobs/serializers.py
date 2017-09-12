from django.contrib.auth import get_user_model
from django.db.models import Q
from django_mysql.models import (
	JSONField,
	ListCharField
	)
from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)
from .models import (
	Job,
	Application
	)
from employers.serializers import (
	EmployerListSerializer,
	)

class ApplicationSerializer(ModelSerializer):
	class Meta:
		model = Application
		fields = ['id', 'seeker', 'job', 'application_status', 'applied_at']
		extra_kwargs = {
		 "application_status":{"read_only":True},
		 "seeker":{"read_only":True}
		}

class JobDetailSerializer(ModelSerializer):
	class Meta:
		model = Job
		fields = ['employer', 'job_title', 'job_type', 'job_status', 'description', 'opening_count',
		'urgent', 'address', 'station', 'incentive', 'start_date', 'hour_wage_low', 'hour_wage_high',
		'req_gender', 'req_education', 'req_japanese_lang_level', 'req_jlpt', 'req_lang', 'req_experience',
		'preferred_certification', 'created_at', 'updated_at']
		extra_kwargs = {
		"employer":{"read_only":True}
		}

	# def create(self, validated_data):
	# 	print("called cre")
	# 	user = None
	# 	request = self.context.get("request")
	# 	if request and hasattr(request,"user"):
	# 		user = request.user
	# 	validated_data["employer"] = user
	# 	return validated_data

	# def save(self, **kwargs):
	# 	self.save()

class JobListSerializer(ModelSerializer):
	employer_name = SerializerMethodField()
	url = HyperlinkedIdentityField(
		view_name = 'jobs-api:rud')
	class Meta:
		model = Job
		fields = ['job_title', 'job_type', 'opening_count', 'employer_name', 'url']
	def get_employer_name(self, obj):
		return str(obj.employer.name)
