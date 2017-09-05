from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.EmployerListView.as_view()),#, name = 'list'
	url(r'^(?P<pk>[\d]+)/$', views.EmployerDetailView.as_view(), name='detail'),
	url(r'^register/$', views.EmployerCreateView.as_view(), name='register'),
	url(r'^login/$', views.EmployerLoginView.as_view(), name='login'),
	url(r'^(?P<pk>[\d]+)/update/$', views.EmployerUpdateView.as_view(), name='update'),
	url(r'^(?P<pk>[\d]+)/delete/$', views.EmployerDeleteView.as_view(), name='delete'),
]

