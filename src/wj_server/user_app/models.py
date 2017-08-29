from django.db.models import (
	BooleanField,
	CharField,
	EmailField,
	FilePathField,
	IntegerField, 
	DateField,
	DateTimeField, 
	Model,
	OneToOneField
)
from django_mysql.models import (
	JSONField,
	ListCharField
)
from django.conf import settings
from django.db.models.signals import post_save
from job_app.models import JobProfile

User = settings.AUTH_USER_MODEL

class UserProfile(Model):
	# user = OneToOneField(User)
	name = CharField(max_length=50,null=False,unique=False)
	gender = CharField(max_length=6,null=False)
	dob = DateField(null=True)
	user_status = CharField(max_length=10,null=False)
	#contact
	email = EmailField(null=False,unique=True)
	contact_number = CharField(max_length=10,null=False,unique=True)
	station_home = CharField(max_length=20,null=True)
	address = CharField(max_length=100,null=True)
	#skill
	education = CharField(max_length=20,null=True)
	# skill = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	# certification = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	japanese_lang_level = IntegerField(null=True)
	# jlpt_score = IntegerField(null=True)
	# language_know = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	job_interested = ListCharField(null=True,base_field=CharField(max_length=10),size=10,max_length=(10*11))
	# job_experienced = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	urgent = BooleanField(default=False)
	experience_level = BooleanField(default=False)
	#file path
	profile_pic_path = FilePathField(null=True)
	identity_proof_path = FilePathField(null=True)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)
	display_lang = CharField(max_length=10,null=True)

	def __str__(self):
		return self.email

# def post_save_user_receiver(sender, instance, created, *args, **kwargs):
# 	if created:
# 		profile, is_created = UserProfile.objects.get_or_create(user=instance)
# post_save.connect(post_save_user_receiver, sender=User)


class JobApplied(Model):
		user_profile_id = OneToOneField(UserProfile)
		job_profile_id = OneToOneField(JobProfile)
		job_applied_status = CharField(max_length=10,null=False)
		applied_at = DateTimeField(auto_now_add=True)