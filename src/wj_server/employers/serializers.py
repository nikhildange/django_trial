from django.contrib.auth import get_user_model
from django.db.models import Q
from django_mysql.models import (
	JSONField
	)
from rest_framework.serializers import (
	CharField,
	EmailField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)
from .models import Employer

User = get_user_model()

class EmployerDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
		'username',
		'email',
		]
		
class EmployerDetailSerializer(ModelSerializer):
	user = EmployerDetailSerializer(read_only=True)
	class Meta:
		model = Employer
		fields = ['user', 'contact_number', 'address', 'created_at']

class EmployerListSerializer(ModelSerializer):
	username = SerializerMethodField()
	employer_id = SerializerMethodField()
	class Meta:
		model = Employer
		fields = ['employer_id','username']
	def get_employer_id(self, obj):
		return str(obj.user.id)
	def get_username(self, obj):
		return str(obj.user.username)


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
		data["token"] = "RANDOM TOKEN"				
		return data

class EmployerCreateSerializer(ModelSerializer):
	username = CharField(source='user.username')
	email = EmailField(source='user.email')
	password = CharField(source='user.password')
	class Meta:
		model = Employer
		fields = [
		'username',
		'email',
		'password',
		'contact_number',
		'address',
		]
		extra_kwargs = {"password":
							{"write_only": True},
						"address":
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
		username = user['username']
		email = user['email']
		password = user['password']
		contact_number = validated_data['contact_number']
		address = validated_data['address']
		print(address)
		user_obj = User(
			username = username,
			email = email,
			)
		user_obj.set_password(password)
		user_obj.save()
		employer_obj = Employer(
			user = user_obj,
			contact_number = contact_number,
			address = address
			)
		employer_obj.save()
		return validated_data
