from rest_framework.pagination import (
	PageNumberPagination,
	)

class JobListPagination(PageNumberPagination):
	page_size = 2
		