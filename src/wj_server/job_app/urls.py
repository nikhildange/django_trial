from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.JobProfileList.as_view()),
	url(r'^(?P<pk>[0-9]+)/$',views.JobProfileDetail.as_view()),
]