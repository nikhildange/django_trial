from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.UserProfileList.as_view()),
	url(r'^(?P<pk>[0-9]+)/$',views.UserProfileDetail.as_view()),
	url(r'^jobs/$',views.UserJobList.as_view()),
	url(r'^jobs/(?P<pk>[0-9]+)/$',views.UserJobDestroy.as_view()),
]