from rest_framework.pagination import (
	PageNumberPagination,
	)

class SeekerListPagination(PageNumberPagination):
	page_size = 10
	class Meta:
		ordering = ['-id']