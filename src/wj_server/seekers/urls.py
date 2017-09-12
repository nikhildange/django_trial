from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.SeekerListView.as_view(), name='list'),
	url(r'^(?P<pk>[\d]+)/$', views.SeekerRUDView.as_view(), name='rud'),
	url(r'^register/$', views.SeekerCreateView.as_view(), name='register'),
	url(r'^login/$', views.SeekerLoginView.as_view(), name='login'),
]