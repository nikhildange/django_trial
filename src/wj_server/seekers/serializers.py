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
	Seeker
	)

User = get_user_model()

class SeekerDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
		'first_name',
		'last_name',
		'email',
		]

class SeekerDetailSerializer(ModelSerializer):
	user = SeekerDetailSerializer(read_only=True)
	class Meta:
		model = Seeker
		fields = ['user', 'gender', 'dob', 'seeker_status', 'contact_number', 'station_home',
		'education', 'certification', 'japanese_lang_level', 'jlpt_score',
		'language_know', 'job_interested', 'job_experienced', 
		'current_salary', 'urgent', 
		'profile_pic_path', 'residance_card_path',
		'created_at', 'updated_at', 'last_applied_at', 'last_login', 
		'display_lang', 'fb_access_token']

class SeekerListSerializer(ModelSerializer):
	first_name = SerializerMethodField()
	last_name = SerializerMethodField()
	seeker_id = SerializerMethodField()
	class Meta:
		model = Seeker
		fields = ['seeker_id', 'first_name', 'last_name']
	def get_seeker_id(self, obj):
		return str(obj.user.id)
	def get_first_name(self, obj):
		return str(obj.user.first_name)
	def get_last_name(self, obj):
		return str(obj.user.last_name)


class SeekerLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	email = CharField(required=True, allow_blank=False)
	class Meta:
		model = User
		fields = ['email',
		'password',
		'token']
		extra_kwargs = {
						"password":
							{"write_only":True},
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
		data["token"] = "RANDOM TOKEN"				
		return data

class SeekerCreateSerializer(ModelSerializer):
	first_name = CharField(source='user.first_name')
	last_name = CharField(source='user.last_name')
	email = EmailField(source='user.email')
	password = CharField(source='user.password')
	class Meta:
		model = Seeker
		fields = [
		'first_name',
		'last_name',
		'email',
		'password'
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

	def validated_contact_number(self, value):
		# field_data = self.get_initial().get('email')
		contact_number = value
		contact_number_qs = User.objects.filter(contact_number=contact_number)
		if contact_number_qs.exists():
			raise ValidationError("This Contact Number Exists.")
		return value
	
	def create(self, validated_data):
		user = validated_data['user']
		first_name = user['first_name']
		last_name = user['last_name']
		email = user['email']
		password = user['password']
		user_obj = User(
			first_name = first_name,
			last_name = last_name,
			email = email,
			)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data
