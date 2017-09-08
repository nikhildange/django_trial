from django.db.models import (
	BooleanField,
	CharField,
	DateField,
	DateTimeField,
	ForeignKey,
	IntegerField, 
	Model,
	)
from django_mysql.models import (
	JSONField,
	ListCharField
	)
from seekers.models import Seeker
from employers.models import Employer
# Create your models here.

class Job(Model):
	employer = ForeignKey(Employer)
	job_title = CharField(max_length=20,null=False)
	job_type = CharField(max_length=20,null=False)
	job_status = CharField(max_length=10,null=False)
	description = CharField(max_length=200,null=False)
	opening_count = IntegerField(null=True)
	urgent = BooleanField(default=False)
	work_time = JSONField(null=True)
	address = CharField(max_length=100,null=True)
	station = CharField(max_length=20,null=True)
	incentive = CharField(max_length=100,null=True)
	start_date = DateField(null=True)
	#salary
	hour_wage_low = IntegerField(null=True)
	hour_wage_high = IntegerField(null=True)
	#Required Skills
	req_gender = CharField(max_length=6,null=True)
	req_education = CharField(max_length=20,null=True)
	req_japanese_lang_level = IntegerField(null=True)
	req_jlpt = IntegerField(null=True)
	req_lang = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	req_experience = ListCharField(base_field=CharField(max_length=10),size=5,max_length=(5*11))
	preferred_certification = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		return self.job_type + ' ' + self.job_title

class Application(Model):
	seeker = ForeignKey(Seeker)
	job = ForeignKey(Job)
	application_status = CharField(max_length=10,null=False,default="active")
	applied_at = DateTimeField(auto_now_add=True)