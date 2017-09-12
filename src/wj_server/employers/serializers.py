from django.contrib.auth import get_user_model
from django.db.models import Q
from django_mysql.models import (
	JSONField
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
from .models import Employer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
User = get_user_model()

class EmployerInfoSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
		'id',
		]
		
class EmployerDetailSerializer(ModelSerializer):
	user = EmployerInfoSerializer(read_only=True)
	email = SerializerMethodField()
	class Meta:
		model = Employer
		fields = ['user', 'email', 'contact_number', 'address', 'created_at']
	def get_email(self, obj):
		return str(obj.user.email)

class EmployerListSerializer(ModelSerializer):
	email = SerializerMethodField()
	employer_id = SerializerMethodField()
	url = HyperlinkedIdentityField(
		view_name = 'employers-api:rud')
	class Meta:
		model = Employer
		fields = ['employer_id','email','url']
	def get_employer_id(self, obj):
		return str(obj.user.id)
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
	token = CharField(allow_blank=True, read_only=True)
	email = EmailField(source='user.email')
	password = CharField(source='user.password')
	name = CharField(source='Employer.name')
	contact_number = CharField(source='Employer.contact_number')
	address = CharField(source='Employer.address')
	class Meta:
		model = Employer
		fields = [
		'name',
		'email',
		'password',
		'contact_number',
		'address',
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
		contact_number = self.get_initial().get('contact_number')
		contact_number_qs = Employer.objects.filter(contact_number=contact_number)
		if contact_number_qs.exists():
			raise ValidationError("This Contact Number Exists.")
		return data
	
	def create(self, validated_data):
		user = validated_data['user']
		email = user['email']
		password = user['password']
		employer = validated_data['Employer']
		name = employer['name']
		contact_number = employer['contact_number']
		address = employer['address']
		user_obj = User(
			email = email,
			is_staff = True,
			)
		user_obj.set_password(password)
		user_obj.save()
		employer_obj = Employer(
			user = user_obj,
			name = name,
			contact_number = contact_number,
			address = address
			)
		employer_obj.save()
		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)
		validated_data["token"] = token
		return validated_data
