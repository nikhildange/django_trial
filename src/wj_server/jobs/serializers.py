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
		fields = [
		'id',
		'seeker', 
		'job', 
		'application_status', 
		'created_at'
		]
		extra_kwargs = {
		 "application_status":{"read_only":True},
		 "seeker":{"read_only":True},
		 "created_at":{"read_only":True}
		}

class JobDetailSerializer(ModelSerializer):
	class Meta:
		model = Job
		fields = [
		'employer',
		'job_title',
		'job_type',
		'job_description',
		'job_status',
		'selling_point',
		'work_time',
		'req_gender',
		'req_education',
		'req_lang',
		'req_japanese_lang_level',
		'req_jlpt',
		'preferred_certificate',
		'hour_wage_low',
		'hour_wage_high',
		'training_need',
		'training_day',
		'training_hour_wage_low',
		'training_hour_wage_high',
		'opening_count',
		'urgent',
		'start_date',
		'rejected_lession',
		'start_date',
		'is_disabled',
		'work_brand_name',
		'work_name',
		'work_address',
		'work_phone_number',
		'work_fax_number',
		'work_train',
		'interview_name',
		'interview_address',
		'interview_phone_number',
		'interview_fax_number',
		'interview_train',
		'created_at',
		'updated_at'
		]
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
	employer_first_name = SerializerMethodField()
	url = HyperlinkedIdentityField(
		view_name = 'jobs-api:rud')
	class Meta:
		model = Job
		fields = ['job_title', 'job_type', 'opening_count', 'employer_first_name', 'work_address', 'url']
	def get_employer_first_name(self, obj):
		return str(obj.employer.user.first_name)
