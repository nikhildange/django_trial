from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import (
	BooleanField,
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)
from rest_framework_jwt.settings import api_settings
from .models import Employer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()
		
class EmployerDetailSerializer(ModelSerializer):
	employer_id = SerializerMethodField()
	email = EmailField(source="user.email")
	first_name = CharField(source="user.first_name")
	last_name = CharField(source="user.last_name")
	class Meta:
		model = Employer
		fields = [
		'employer_id',
		'email',
		'first_name',
		'last_name', 
		'phone_number', 
		'fax_number', 
		'is_admin', 
		'is_disabled',
		]
	def get_employer_id(self, obj):
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
			Employer.objects.filter(pk=instance.user.pk).update(**validated_data)
		return instance

class EmployerListSerializer(ModelSerializer):
	employer_id = SerializerMethodField()
	first_name = SerializerMethodField()
	email = SerializerMethodField()
	url = HyperlinkedIdentityField(
		view_name = 'employers-api:rud')
	class Meta:
		model = Employer
		fields = ['employer_id', 'first_name', 'email', 'url']
	def get_employer_id(self, obj):
		return str(obj.user.id)
	def get_first_name(self, obj):
		return str(obj.user.first_name)
	def get_email(self, obj):
		return str(obj.user.email)


class EmployerLoginSerializer(ModelSerializer):
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
		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)
		data["token"] = token				
		return data

class EmployerCreateSerializer(ModelSerializer):
	email = EmailField(source='user.email')
	first_name = CharField(source='user.first_name')
	last_name = CharField(source='user.last_name')
	phone_number = CharField(source='Employer.phone_number')
	fax_number = CharField(source='Employer.fax_number')
	is_admin = BooleanField(source='Employer.is_admin')
	password = CharField(source='user.password')
	token = CharField(allow_blank=True, read_only=True)
	class Meta:
		model = Employer
		fields = [
		'email',
		'first_name',
		'last_name', 

		'phone_number', 
		'fax_number', 
		'is_admin',
		'password',
		'token',
		]
		extra_kwargs = {"password":
							{"write_only": True}
						}

	def validate_email(self, value):
		email = value
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise ValidationError("This Email Exists.")
		return value

	def validate(self, data):
		phone_number = self.get_initial().get('phone_number')
		phone_number_qs = Employer.objects.filter(phone_number=phone_number)
		if phone_number_qs.exists():
			raise ValidationError("This phone Number Exists.")
		fax_number = self.get_initial().get('fax_number')
		fax_number_qs = Employer.objects.filter(fax_number=fax_number)
		if fax_number_qs.exists():
			raise ValidationError("This Fax Number Exists.")
		return data

	def create(self, validated_data):
		user = validated_data['user']
		email = user['email']
		password = user['password']
		first_name = user['first_name']
		last_name = user['last_name']
		employer = validated_data['Employer']
		phone_number = employer['phone_number']
		fax_number = employer['fax_number']
		is_admin = employer['is_admin']
		user_obj = User(
			email=email,
			is_staff=True,
			first_name=first_name,
			last_name=last_name
			)
		user_obj.set_password(password)
		user_obj.save()
		employer_obj = Employer(
			user = user_obj,
			phone_number = phone_number,
			fax_number = fax_number,
			is_admin = is_admin
			)
		employer_obj.save()
		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)
		validated_data["token"] = token
		return validated_data
