from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.JobListView.as_view(), name = 'list'),
	url(r'^(?P<pk>[\d]+)/$', views.JobDetailView.as_view(), name='detail'),
	url(r'^create/$', views.JobCreateView.as_view(), name='create'),
	url(r'^(?P<pk>[\d]+)/update/$', views.JobUpdateView.as_view(), name='update'),
	url(r'^(?P<pk>[\d]+)/delete/$', views.JobDeleteView.as_view(), name='delete'),
	url(r'^applications/$', views.ApplicationListView.as_view(), name='application_list'),
	url(r'^applications/subscribe/$', views.ApplicationCreateView.as_view(), name='subscrice_job'),
	url(r'^applications/(?P<pk>[\d]+)/$', views.ApplicationDestroyView.as_view(), name='unsubscrice_job'),
]