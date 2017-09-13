from django.http import (
	JsonResponse,
	)
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


def work_time_format():
	return {{"day":"","start_time":"","end_time":""}}

def address_format():
 	return {"postal_code":"","prefecture":"","city":"","lot_number":"","building_name":""}

def near_train_station_format():
	return {"near_station":"","near_station_exit_name":"","near_station_transit_time":""}

class Job(Model):
	employer = ForeignKey(Employer)
	job_title = CharField(max_length=20,null=False)
	job_type = CharField(max_length=20,null=False)
	job_description = CharField(max_length=200,blank=True)
	job_status = CharField(max_length=10,default="active")
	selling_point = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),blank=True)
	work_time = JSONField(blank=True,null=True)
	opening_count = IntegerField(blank=True)
	urgent = BooleanField(default=False)
	start_date = DateField(blank=True)
	is_disabled = BooleanField(default=False)
	rejected_lession = CharField(max_length=100,blank=True)
	#salary
	hour_wage_low = IntegerField(null=True)
	hour_wage_high = IntegerField(null=True)
	training_need = BooleanField(default=False)
	training_day = IntegerField(null=True)
	training_hour_wage_low = IntegerField(null=True)
	training_hour_wage_high = IntegerField(null=True)
	#required
	req_gender = CharField(max_length=6,blank=True)
	req_education = CharField(max_length=20,blank=True)
	req_japanese_lang_level = IntegerField(blank=True)
	req_jlpt = IntegerField(null=True)
	req_lang = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	req_experience = ListCharField(base_field=CharField(max_length=10),size=5,max_length=(5*11),null=True)
	preferred_certificate = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	#work
	work_brand_name = CharField(max_length=15,blank=True)
	work_name = CharField(max_length=15,blank=True)
	work_address = JSONField(blank=True,null=True)
	work_phone_number = CharField(max_length=10,blank=True)
	work_fax_number = CharField(max_length=10,blank=True)
	work_train = JSONField(blank=True,null=True)
	#interview
	interview_name = CharField(max_length=15,blank=True)
	interview_address = JSONField(blank=True,null=True)
	interview_phone_number = CharField(max_length=10,blank=True)
	interview_fax_number = CharField(max_length=10,blank=True)
	interview_train = JSONField(blank=True,null=True)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)

	def __str__(self):
		return self.job_type + ' -> ' + self.job_title

class Application(Model):
	seeker = ForeignKey(Seeker,null=False)
	job = ForeignKey(Job,null=False)
	application_status = CharField(max_length=10,blank=False,default="active")
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)
	class Meta:
		unique_together = ('seeker','job')