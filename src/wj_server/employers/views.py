from django.contrib.auth import get_user_model
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
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

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
	EmployerCreateSerializer,
	EmployerListSerializer,
	EmployerLoginSerializer,
	EmployerDetailSerializer,
	)

class EmployerCreateView(CreateAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerCreateSerializer
	permission_classes = [AllowAny]

class EmployerListView(ListAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerListSerializer
	permission_classes = [IsAdminUser]
	pagination_class = EmployerListPagination

class EmployerDetailView(RetrieveAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsAdminUser]

class EmployerUpdateView(RetrieveUpdateAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsOwnerOrReadOnly, IsAdminUser]

class EmployerDeleteView(DestroyAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsAdminUser]
		
class EmployerLoginView(APIView):
	serializer_class = EmployerLoginSerializer
	permission_classes = [AllowAny]

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = EmployerLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

