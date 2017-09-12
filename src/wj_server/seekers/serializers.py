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
from rest_framework_jwt.settings import api_settings
from .models import (
	Seeker
	)

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()

class SeekerInfoSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
		'id',
		]

class SeekerDetailSerializer(ModelSerializer):
	user = SeekerInfoSerializer(read_only=True)
	email = SerializerMethodField()
	class Meta:
		model = Seeker
		fields = ['user', 'email', 'name', 'gender', 'dob', 'seeker_status', 'contact_number', 'station_home',
		'education', 'certification', 'japanese_lang_level', 'jlpt_score',
		'language_know', 'job_interested', 'job_experienced', 
		'current_salary', 'urgent', 
		'profile_pic_path', 'residance_card_path',
		'created_at', 'updated_at', 'last_applied_at', 'last_login', 
		'display_lang', 'fb_access_token']
	def get_email(self, obj):
		return str(obj.user.email)

class SeekerListSerializer(ModelSerializer):
	seeker_id = SerializerMethodField()
	seeker_email = SerializerMethodField()
	url = HyperlinkedIdentityField(
		view_name = 'seekers-api:rud')
	class Meta:
		model = Seeker
		fields = ['seeker_id', 'name', 'seeker_email', 'url', 'contact_number', 'display_lang']
	def get_seeker_id(self, obj):
		return str(obj.user.id)
	def get_seeker_email(self, obj):
		return str(obj.user.email)

class SeekerLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	email = CharField(required=True, allow_blank=False)
	class Meta:
		model = User
		fields = ['email',
		'password',
		'token']
		extra_kwargs = {"password":
							{"write_only": True}
						}
						
	def validate(self, data):
		email = data.get("email", None)
		password = data.get("password", None)
		if not email and not password:
			raise ValidationError("Email and Password Required")
		user = User.objects.filter(
				Q(email=email)
			).distinct()
		if user.exists() and user.count() == 1:
			user_obj = user.first()
		else:
			raise ValidationError("Invalid Email Address")
		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Incorrect Credential. Please Try Again")
		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)
		data["token"] = token		
		return data

class SeekerCreateSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	email = EmailField(source='user.email')
	password = CharField(source='user.password')
	class Meta:
		model = Seeker
		fields = [
		'email',
		'password',
		'token',
		]
		extra_kwargs = {"password":
							{"write_only": True}
						}

	# def validate(self, data):
	# 	email = data['email']
	# 	return data

	def validate_email(self, value):
		email = value
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise ValidationError("This Email Exists.")
		return value

	def create(self, validated_data):
		user = validated_data['user']
		email = user['email']
		password = user['password']
		user_obj = User(
			email = email,
			is_staff = True,
			)
		user_obj.set_password(password)
		user_obj.save()
		seeker_obj = Seeker(
			user = user_obj,
			)
		seeker_obj.save()
		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)
		validated_data["token"] = token
		return validated_data
