from django.db.models import (
	CharField,
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
	user = OneToOneField(User)
	name = CharField(max_length=50,null=False,unique=True)
	gender = CharField(max_length=10,null=False)
	dob = DateField(null=True)
	contact_number = CharField(max_length=10,null=False)
	current_salary = IntegerField(null=True)
	station_home = CharField(max_length=20,null=False)
	station_school = CharField(max_length=20,null=False)
	education = CharField(max_length=20,null=False)
	skill = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	certification = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	japanese_lang_level = IntegerField(null=True)
	jlpt_score = IntegerField(null=True)
	language_know = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	job_interested = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	job_experienced = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	user_img_files = JSONField()#default={‘profile_pic’:’’,’visa_pic’:’’,’residance_card_pic’:’’,’self_intro_voice’:’’})
	created_on = DateTimeField(auto_now_add=True)
	last_updated = DateTimeField(auto_now=True)
	display_lang = CharField(max_length=10,null=False)

	def __str__(self):
		return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		profile, is_created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)



class JobApplied(Model):
		user_profile_id = OneToOneField(UserProfile)
		job_profile_id = OneToOneField(JobProfile)
		applied_at = DateTimeField(auto_now_add=True)