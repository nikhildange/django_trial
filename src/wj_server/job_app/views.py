from rest_framework import generics
from .models import JobProfile
from .serializers import JobProfileSerializer

class JobProfileList(generics.ListCreateAPIView):
	queryset = JobProfile.objects.all()
	serializer_class = JobProfileSerializer

class JobProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = JobProfile.objects.all()
	serializer_class = JobProfileSerializer