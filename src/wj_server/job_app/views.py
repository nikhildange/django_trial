from django.conf import settings
from django.db.models import Q
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
	)
from rest_framework.generics import (
	# RetrieveUpdateDestroyAPIView,
	CreateAPIView,
	DestroyAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	UpdateAPIView,
	ListAPIView,
	)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .models import JobProfile
from .permissions import IsOwnerOrReadOnly
from .serializers import (
	JobProfileCreateUpdateSerializer,
	JobProfileSerializer
)

class JobProfileCreate(CreateAPIView):
	queryset = JobProfile.objects.all()
	serializer_class = JobProfileCreateUpdateSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]
	def perform_create(self, serializer):
		serializer.save(job_status="active")
		# serializer.save(user=user.request.user)

class JobProfileDestroy(DestroyAPIView):
	queryset = JobProfile.objects.all()
	serializer_class = JobProfileSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

class JobProfileDetail(RetrieveAPIView):
	queryset = JobProfile.objects.all()
	serializer_class = JobProfileSerializer
	lookup_field = 'job_type'

class JobProfileUpdate(RetrieveUpdateAPIView):
	queryset = JobProfile.objects.all()
	serializer_class = JobProfileCreateUpdateSerializer
	permission_classes = [IsOwnerOrReadOnly]

class JobProfileList(ListAPIView):
	serializer_class = JobProfileSerializer
	permission_classes = [AllowAny]
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['job_type','job_title','id',]

	def get_queryset(self, *args, **kwargs):
		# queryset_list = super(JobProfileList, self).get_queryset(*args,*kwargs)
		queryset_list = JobProfile.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(job_type__icontains=query) |
				Q(job_title__icontains=query) |
				Q(job_status__icontains=query) 
				# Q(recruiter__email__icontains=query)
				).distinct()
		return queryset_list
