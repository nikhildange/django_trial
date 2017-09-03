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

class RecruiterProfile(Model):
	user = OneToOneField(settings.AUTH_USER_MODEL, default=1)
	# name = CharField(max_length=50, null=False, unique=True)
	#contact
	# email = EmailField(null=False, unique=True)
	contact_number = CharField(max_length=10, null=False, unique=True)
	address = CharField(max_length=100, null=False)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.email

class JobProfile(Model):
	recruiter = ForeignKey(RecruiterProfile)
	job_title = CharField(max_length=20,null=False)
	job_type = CharField(max_length=20,null=False)
	job_status = CharField(max_length=10,null=False)
	#description
	opening_count = IntegerField(null=True)
	urgent = BooleanField(default=False)
	work_time = JSONField(null=True)
	address = CharField(max_length=100,null=True)
	address_coordinate = JSONField(null=True)
	station = CharField(max_length=20,null=True)
	#salary
	hour_wage_low = IntegerField(null=True)
	hour_wage_high = IntegerField(null=True)
	#Required Skills
	req_gender = CharField(max_length=6,null=True)
	req_education = CharField(max_length=20,null=True)
	req_japanese_lang_level = IntegerField(null=True)
	req_experience_level = BooleanField(default=False)
	# skill = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	# certification = ListCharField(base_field=CharField(max_length=10),size=10)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)
