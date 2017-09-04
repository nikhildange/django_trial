from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)

class JobProfileLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 10
	max_limit = 10

class JobProfilePageNumberPagination(PageNumberPagination):
	page_size = 10