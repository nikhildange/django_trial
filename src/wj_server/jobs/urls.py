from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.JobListView.as_view(), name = 'list'),
	url(r'^(?P<pk>[\d]+)/$', views.JobRUDView.as_view(), name='rud'),
	url(r'^create/$', views.JobCreateView.as_view(), name='create'),
	
	url(r'^applications/$', views.ApplicationListView.as_view(), name='job_app_list'),
	url(r'^applications/subscribe/$', views.ApplicationCreateView.as_view(), name='subscribe_job_app'),
	url(r'^applications/(?P<pk>[\d]+)/$', views.ApplicationRDView.as_view(), name='unsubscribe_job_app')
]