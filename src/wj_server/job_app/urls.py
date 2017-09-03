from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.JobProfileList.as_view()),
	url(r'^create/$',views.JobProfileCreate.as_view()),
	url(r'^(?P<job_type>[\w-]+)/$',views.JobProfileDetail.as_view()),
	url(r'^delete/(?P<pk>[\d]+)/$',views.JobProfileDestroy.as_view()),
	url(r'^update/(?P<pk>[0-9]+)/$',views.JobProfileUpdate.as_view()),
	# url(r'^(?P<pk>[0-9]+)/$',views.JobProfileDetail.as_view()),
]