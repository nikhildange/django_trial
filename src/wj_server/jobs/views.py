from django.contrib.auth import get_user_model
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	RetrieveDestroyAPIView,
	RetrieveUpdateDestroyAPIView,
	ListAPIView,
	)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from employers.models import (
	Employer,
)
from seekers.models import (
	Seeker,
)

from .models import (
	Application,
	Job,
	)
from .pagination import (
	JobListPagination,
	)
from .permissions import (
	IsEmployer,
	IsSeeker,
	)
from .serializers import (
	ApplicationSerializer,
	JobListSerializer,
	JobDetailSerializer,
	)

class JobCreateView(CreateAPIView):
	queryset = Job.objects.all()
	serializer_class = JobDetailSerializer
	permission_classes = [IsEmployer]

	def perform_create(self, serializer):
		employer = Employer.objects.get(user=self.request.user)
		serializer.save(employer=employer)

class JobListView(ListAPIView):
	queryset = Job.objects.all()
	serializer_class = JobListSerializer
	pagination_class = JobListPagination
	permission_classes = [IsAuthenticated]

class JobRUDView(RetrieveUpdateDestroyAPIView):
	queryset = Job.objects.all()
	serializer_class = JobDetailSerializer
	permission_classes = [IsEmployer]


class ApplicationCreateView(CreateAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer
	permission_classes = [IsSeeker]

	def perform_create(self, serializer):
		seeker = Seeker.objects.get(user=self.request.user)
		serializer.save(seeker=seeker)

class ApplicationListView(ListAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer
	permission_classes = [IsAuthenticated]

class ApplicationRDView(RetrieveDestroyAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer
	permission_classes = [IsSeeker]