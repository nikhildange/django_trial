from rest_framework import generics
from .models import UserProfile, JobApplied
from .permissions import IsAdminOrReadOnly
from .serializers import UserProfileSerializer, UserJobSerializer

class UserProfileList(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = (IsAdminOrReadOnly,)

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = (IsAdminOrReadOnly,)

class UserJobList(generics.ListCreateAPIView):
	queryset = JobApplied.objects.all()
	serializer_class = UserJobSerializer
	permission_classes = (IsAdminOrReadOnly,)

class UserJobDestroy(generics.DestroyAPIView):
	queryset = JobApplied.objects.all()
	serializer_class = UserJobSerializer
	permission_classes = (IsAdminOrReadOnly,)
		