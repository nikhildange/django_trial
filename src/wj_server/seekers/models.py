from django.conf import settings
# from django.db.models.signals import post_delete
from django.db.models import (
	BooleanField,
	CASCADE,
	CharField,
	EmailField,
	FilePathField,
	ForeignKey,
	IntegerField,
	DateField,
	DateTimeField,
	ManyToManyField, 
	Model,
	OneToOneField
)
from django_mysql.models import (
	JSONField,
	ListCharField
)

User = settings.AUTH_USER_MODEL

def near_station():
	return {"near_prefecture":"","near_city":"","near_station":""}

class Seeker(Model):
	user = OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=CASCADE)
	gender = CharField(max_length=6,null=True)
	dob = DateField(null=True)
	nationality = CharField(max_length=10,null=True)
	visa_type = CharField(max_length=10,null=True)
	#contact
	phone_number = CharField(max_length=10,null=True,unique=True)
	phone_country_code = CharField(max_length=5,null=True)
	near_station = JSONField(default=near_station)
	#skill
	education = CharField(max_length=20,null=True)
	certificate = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	japanese_lang_level = IntegerField(null=True)
	jlpt_score = IntegerField(null=True)
	lang_known = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	job_interested = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	job_experienced = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	current_hourly_salary = IntegerField(null=True)
	#file path
	id_photo_path = FilePathField(blank=True,null=True)
	profile_pic_path = FilePathField(blank=True,null=True)
	residence_card_path = FilePathField(blank=True,null=True)
	intro_voice_path = FilePathField(blank=True,null=True)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)
	last_application = DateTimeField(null=True)
	last_login = DateTimeField(auto_now=True)
	is_disabled = BooleanField(default=False)
	disp_lang = CharField(max_length=10,null=True)
	seeker_status = CharField(max_length=10,null=True)
	urgent = BooleanField(default=False)
	#token
	fb_access_token = CharField(max_length=255,null=True)

	def __str__(self):
		return self.user.email

	# def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	# 	if created:
	# 		profile, is_created = Seeker.objects.get_or_create(user=instance)
	# post_save.connect(post_save_user_receiver, sender=User)
        