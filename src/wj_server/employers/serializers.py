from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,
	)
from .models import Employer

class EmployerDetailSerializer(ModelSerializer):
	username = SerializerMethodField()
	email = SerializerMethodField()
	class Meta:
		model = Employer
		fields = ['id', 'username', 'email', 'contact_number', 'address', 'created_at', 'user']
	def get_username(self, obj):
		return str(obj.user.username)
	def get_email(self, obj):
		return str(obj.user.email)

class EmployerListSerializer(ModelSerializer):
	username = SerializerMethodField()
	class Meta:
		model = Employer
		fields = ['id', 'username']
	def get_username(self, obj):
		return str(obj.user.username)