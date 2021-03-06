from rest_framework.pagination import (
	PageNumberPagination,
	)

class EmployerListPagination(PageNumberPagination):
	page_size = 10
	class Meta:
		ordering = ['-id']