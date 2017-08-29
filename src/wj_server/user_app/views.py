from rest_framework import generics
from .models import UserProfile, JobApplied
from .serializers import UserProfileSerializer, UserJobSerializer

class UserProfileList(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer

class UserJobList(generics.ListCreateAPIView):
	queryset = JobApplied.objects.all()
	serializer_class = UserJobSerializer

class UserJobDestroy(generics.DestroyAPIView):
	queryset = JobApplied.objects.all()
	serializer_class = UserJobSerializer
		