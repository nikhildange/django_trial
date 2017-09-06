from django.contrib.auth import get_user_model
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
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

from .models import (
	Application,
	Job,
	)
from .pagination import (
	JobListPagination,
	)
from .serializers import (
	ApplicationSerializer,
	JobListSerializer,
	JobDetailSerializer,
	)

class JobCreateView(CreateAPIView):
	queryset = Job.objects.all()
	serializer_class = JobDetailSerializer
	permission_classes = [AllowAny]

class JobListView(ListAPIView):
	queryset = Job.objects.all()
	serializer_class = JobListSerializer
	permission_classes = [IsAdminUser]
	pagination_class = JobListPagination

class JobDetailView(RetrieveAPIView):
	queryset = Job.objects.all()
	serializer_class = JobDetailSerializer
	permission_classes = [IsAdminUser]

class JobUpdateView(RetrieveUpdateAPIView):
	queryset = Job.objects.all()
	serializer_class = JobDetailSerializer
	permission_classes = [IsAdminUser]#, IsOwnerOrReadOnly]

class JobDeleteView(DestroyAPIView):
	queryset = Job.objects.all()
	serializer_class = JobDetailSerializer
	permission_classes = [IsAdminUser]

class ApplicationListView(ListAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer
	permission_classes = [IsAdminUser]

class ApplicationDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer
	permission_classes = [IsAdminUser]
