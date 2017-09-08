from django.conf import settings
from django.db.models.signals import post_save
from django.db.models import (
	BooleanField,
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
	user = OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	gender = CharField(max_length=6,null=False)
	dob = DateField(null=True)
	seeker_status = CharField(max_length=10,null=False)
	#contact
	contact_number = CharField(max_length=10,null=False,unique=True)
	station_home = CharField(max_length=20,null=True)
	#skill
	education = CharField(max_length=20,null=True)
	certification = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	japanese_lang_level = IntegerField(null=True)
	jlpt_score = IntegerField(null=True)
	language_know = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
	job_interested = ListCharField(null=True,base_field=CharField(max_length=10),size=10,max_length=(10*11))
	job_experienced = ListCharField(base_field=CharField(max_length=10),size=10,max_length=(10*11))
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

	USER_FIELD = 'email'

	def __str__(self):
		return self.user.email

	def post_save_user_receiver(sender, instance, created, *args, **kwargs):
		if created:
			profile, is_created = Seeker.objects.get_or_create(user=instance)
	post_save.connect(post_save_user_receiver, sender=User)