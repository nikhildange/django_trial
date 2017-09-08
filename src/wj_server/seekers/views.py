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
	Seeker,
	)
from .pagination import (
	SeekerListPagination,
	)
from .permissions import (
	IsSeeker
	)
from .serializers import (
	SeekerCreateSerializer,
	SeekerListSerializer,
	SeekerLoginSerializer,
	SeekerDetailSerializer,
	)

class SeekerCreateView(CreateAPIView):
	queryset = Seeker.objects.all()
	serializer_class = SeekerCreateSerializer
	permission_classes = [AllowAny]

class SeekerListView(ListAPIView):
	queryset = Seeker.objects.all()
	serializer_class = SeekerListSerializer
	pagination_class = SeekerListPagination
	permission_classes = [IsAuthenticated]

class SeekerDetailView(RetrieveAPIView):
	queryset = Seeker.objects.all()
	serializer_class = SeekerDetailSerializer
	permission_classes = [IsAuthenticated]

class SeekerUpdateView(RetrieveUpdateAPIView):
	queryset = Seeker.objects.all()
	serializer_class = SeekerDetailSerializer
	permission_classes = [IsSeeker]

class SeekerDeleteView(DestroyAPIView):
	queryset = Seeker.objects.all()
	serializer_class = SeekerDetailSerializer
	permission_classes = [IsSeeker]
		
class SeekerLoginView(APIView):
	serializer_class = SeekerLoginSerializer
	permission_classes = [AllowAny]

	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = SeekerLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
