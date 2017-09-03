from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveUpdateDestroyAPIView,
	DestroyAPIView
	)
from .models import UserProfile, JobApplied
from .permissions import IsAdminOrReadOnly
from .serializers import UserProfileSerializer, UserJobSerializer

class UserProfileList(ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = (IsAdminOrReadOnly,)

class UserProfileDetail(RetrieveUpdateDestroyAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	permission_classes = (IsAdminOrReadOnly,)

class UserJobList(ListCreateAPIView):
	queryset = JobApplied.objects.all()
	serializer_class = UserJobSerializer
	permission_classes = (IsAdminOrReadOnly,)

class UserJobDestroy(DestroyAPIView):
	queryset = JobApplied.objects.all()
	serializer_class = UserJobSerializer
	permission_classes = (IsAdminOrReadOnly,)
		