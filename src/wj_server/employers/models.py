from django.conf import settings
from django.db.models import (
	BooleanField,
	CharField,
	EmailField,
	ForeignKey,
	IntegerField, 
	DateTimeField,
	ManyToManyField, 
	Model,
	OneToOneField
	)
from django_mysql.models import (
	JSONField,
	ListCharField
)

def address_format():
	return {'building':'','district':'','pincode':''}

class Employer(Model):
	user = OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	name = CharField(max_length=20, null=False)
	#
	contact_number = CharField(max_length=10, null=False)
	address = JSONField(default=address_format)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		return self.name