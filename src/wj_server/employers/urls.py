from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.EmployerListView.as_view(), name='list'),
	url(r'^(?P<pk>[\d]+)/$', views.EmployerRUDView.as_view(), name='rud'),
	url(r'^register/$', views.EmployerCreateView.as_view(), name='register'),
	url(r'^login/$', views.EmployerLoginView.as_view(), name='login'),
]

