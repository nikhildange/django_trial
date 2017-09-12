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

class Seeker(Model):
	user = OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=CASCADE)
	name = CharField(max_length=15,null=True)
	gender = CharField(max_length=6,null=True)
	dob = DateField(null=True)
	seeker_status = CharField(max_length=10,null=True)
	#contact
	contact_number = CharField(max_length=10,null=True,unique=True)
	station_home = CharField(max_length=20,null=True)
	#skill
	education = CharField(max_length=20,null=True)
	certification = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	japanese_lang_level = IntegerField(null=True)
	jlpt_score = IntegerField(null=True)
	language_know = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	job_interested = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	job_experienced = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11),null=True)
	current_salary = IntegerField(null=True)
	urgent = BooleanField(default=False)
	#file path
	profile_pic_path = FilePathField(null=True)
	residance_card_path = FilePathField(null=True)
	#time
	created_at = DateTimeField(auto_now_add=True)
	updated_at = DateTimeField(auto_now=True)
	last_applied_at = DateTimeField(auto_now=True)
	last_login = DateTimeField(auto_now=True)
	display_lang = CharField(max_length=10,null=True)
	#token
	fb_access_token = CharField(max_length=255,null=True)

	def __str__(self):
		return self.user.email

	# def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	# 	if created:
	# 		profile, is_created = Seeker.objects.get_or_create(user=instance)
	# post_save.connect(post_save_user_receiver, sender=User)
        