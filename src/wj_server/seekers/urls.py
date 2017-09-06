from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.SeekerListView.as_view()),#, name = 'list'
	url(r'^(?P<pk>[\d]+)/$', views.SeekerDetailView.as_view(), name='detail'),
	url(r'^register/$', views.SeekerCreateView.as_view(), name='register'),
	url(r'^login/$', views.SeekerLoginView.as_view(), name='login'),
	url(r'^(?P<pk>[\d]+)/update/$', views.SeekerUpdateView.as_view(), name='update'),
	url(r'^(?P<pk>[\d]+)/delete/$', views.SeekerDeleteView.as_view(), name='delete'),
]