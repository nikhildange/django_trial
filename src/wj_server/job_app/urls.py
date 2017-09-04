from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.JobProfileList.as_view(), name='read'),
	url(r'^create/$',views.JobProfileCreate.as_view(), name='create'),
	url(r'^(?P<job_type>[\w-]+)/$',views.JobProfileDetail.as_view(), name='detail'),
	url(r'^delete/(?P<pk>[\d]+)/$',views.JobProfileDestroy.as_view(), name='delete'),
	url(r'^update/(?P<pk>[0-9]+)/$',views.JobProfileUpdate.as_view(), name='update'),
	# url(r'^(?P<pk>[0-9]+)/$',views.JobProfileDetail.as_view()),
]