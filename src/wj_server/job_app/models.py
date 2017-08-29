from django.db.models import (
	CharField,
	IntegerField, 
	DateTimeField, 
	Model
)
from django_mysql.models import (
	JSONField,
	ListCharField
)

# Create your models here.
class JobProfile(Model):
	job_title = CharField(max_length=20)#,null=False)
	job_type = CharField(max_length=20)#,null=False)
	# skill = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	# req_lang = ListCharField(base_field=CharField(max_length=10),size=10)
	# min_salary = IntegerField(null=True)
	# max_salary = IntegerField(null=True)
	# landmark = models.CharField(max_length=30,null=False)
	# address = models.CharField(max_length=100,null=False)
	# certification = ListCharField(base_field=CharField(max_length=10),size=10)
	# working_hour_description = models.CharField(max_length=100,null=False)
	# address_coordinate = JSONField()
	# date_job_posted = DateTimeField(auto_now_add=True)
	# job_status = models.CharField(max_length=10,null=False)