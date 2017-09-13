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
		'first_name',
		'last_name',
		'email',
		]

class SeekerDetailSerializer(ModelSerializer):
	seeker_id = SerializerMethodField()
	email = EmailField(source="user.email")
	first_name = CharField(source="user.first_name")
	last_name = CharField(source="user.last_name")
	class Meta:
		model = Seeker
		fields = [
		'seeker_id',
		'email',
		'first_name',
		'last_name',
		'gender',
		'dob',
		'nationality',
		'visa_type',
		'education',
		'certificate',
		'lang_known',
		'japanese_lang_level',
		'jlpt_score',
		'job_interested',
		'job_experienced',
		'current_hourly_salary',
		'phone_country_code',
		'phone_number',
		'id_photo_path',
		'profile_pic_path',
		'residence_card_path',
		'intro_voice_path',
		'near_station', #{“near_prefecture”:””,”near_city”:””,”near_station”:””}
		'fb_access_token',
		'disp_lang',
		'urgent',
		'seeker_status',
		'last_application',
		'last_login',
		'is_disabled',
		'created_at',
		'updated_at'
		]
	def get_seeker_id(self, obj):
		return str(obj.user.id)
	def get_email(self, obj):
		return str(obj.user.email)
	def get_first_name(self, obj):
		return str(obj.user.first_name)
	def get_last_name(self, obj):
		return str(obj.user.last_name)

	def update(self, instance, validated_data):

		if 'user' in validated_data:
			user_value = validated_data["user"]
			User.objects.filter(pk=instance.user.pk).update(**user_value)
			validated_data.pop('user')

		if len(validated_data)>0:
			Seeker.objects.filter(pk=instance.user.pk).update(**validated_data)

		# User.objects.filter(pk=instance.user.pk).update(user_value.keys(),user_value.values())
		# User.objects.filter(pk=instance.user.pk).update(first_name=user_value['first_name'],last_name=user_value['last_name'])
		# print(user_obj)
		# user.first_name = user_obj["first_name"]
		# user.last_name = user_obj["last_name"]
		# user.save(update_fields=['first_name','last_name'])
		# instance.save(update_fields=fields)
		return instance

class SeekerListSerializer(ModelSerializer):
	user = SeekerInfoSerializer(read_only=True)
	url = HyperlinkedIdentityField(
		view_name = 'seekers-api:rud')
	class Meta:
		model = Seeker
		fields = ['user', 'url', 'phone_number', 'disp_lang']

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
