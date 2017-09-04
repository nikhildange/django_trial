from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	ListAPIView,
	)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)
from .models import (
	Employer,
	)
from .pagination import (
	EmployerListPagination,
	)
from .permissions import (
	IsOwnerOrReadOnly
	)
from .serializers import (
	EmployerListSerializer,
	EmployerDetailSerializer,
	)

class EmployerCreateView(CreateAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]

class EmployerListView(ListAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerListSerializer
	permission_classes = [IsAdminUser]
	pagination_class = EmployerListPagination

class EmployerDetailView(RetrieveAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsOwnerOrReadOnly, IsAdminUser]

class EmployerUpdateView(RetrieveUpdateAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsOwnerOrReadOnly, IsAdminUser]

class EmployerDeleteView(DestroyAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
		