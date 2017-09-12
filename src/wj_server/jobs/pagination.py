from rest_framework.pagination import (
	PageNumberPagination,
	)

class JobListPagination(PageNumberPagination):
	page_size = 10
	class Meta:
		ordering = ['-id']
		