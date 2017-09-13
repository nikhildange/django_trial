from django.conf import settings
from django.db.models import (
	BooleanField,
	CharField, 
	DateTimeField,
	Model,
	OneToOneField
	)
from django_mysql.models import (
	JSONField,
	ListCharField
)

class Employer(Model):
	user = OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	#
	phone_number = CharField(max_length=10, null=False)
	fax_number = CharField(max_length=10, null=False)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)
	#
	is_admin = BooleanField(default=False)
	is_disabled = BooleanField(default=False)

	def __str__(self):
		return self.user.email