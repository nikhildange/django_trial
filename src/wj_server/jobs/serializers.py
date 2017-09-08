from django.contrib.auth import get_user_model
from django.db.models import Q
from django_mysql.models import (
	JSONField,
	ListCharField
	)
from rest_framework.serializers import (
	CharField,
	EmailField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)
from .models import (
	Job,
	Application
	)

class ApplicationSerializer(ModelSerializer):
	class Meta:
		model = Application
		fields = ['id', 'seeker', 'job', 'application_status', 'applied_at']
		extra_kwargs = {
		 "application_status":{"read_only":True}
		# "applied_at":{"write_only":True}
		}


class JobDetailSerializer(ModelSerializer):
	class Meta:
		model = Job
		fields = ['employer', 'job_title', 'job_type', 'job_status', 'description', 'opening_count',
		'urgent', 'work_time', 'address', 'station', 'incentive', 'start_date', 'hour_wage_low', 'hour_wage_high',
		'req_gender', 'req_education', 'req_japanese_lang_level', 'req_jlpt', 'req_lang', 'req_experience',
		'preferred_certification', 'created_at', 'updated_at']
		# extra_kwargs = {
		# "created_at":{"write_only":True},
		# "updated_at":{"write_only":True}
		# }


class JobListSerializer(ModelSerializer):
	employer_name = SerializerMethodField()
	class Meta:
		model = Job
		fields = ['job_title', 'job_type', 'opening_count', 'employer_name']
	def get_employer_name(self, obj):
		return str(obj.employer.user.username)
