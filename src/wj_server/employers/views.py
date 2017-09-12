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
from rest_framework.status import HTTP_200_OK, HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import (
	Employer,
	)
from .pagination import (
	EmployerListPagination,
	)
from .permissions import (
	IsEmployer
	)
from .serializers import (
	EmployerCreateSerializer,
	EmployerListSerializer,
	EmployerLoginSerializer,
	EmployerDetailSerializer,
	)

User = get_user_model()

class EmployerCreateView(CreateAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerCreateSerializer
	permission_classes = [AllowAny]

class EmployerListView(ListAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerListSerializer
	pagination_class = EmployerListPagination
	permission_classes = [IsAuthenticated]

class EmployerRUDView(RetrieveUpdateDestroyAPIView):
	queryset = Employer.objects.all()
	serializer_class = EmployerDetailSerializer
	permission_classes = [IsEmployer]

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		print(instance)
		user = User.objects.get(email=instance.user.email)
		print(user)
		self.perform_destroy(instance)
		# user.delete()
		return Response(status=HTTP_202_ACCEPTED)

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

