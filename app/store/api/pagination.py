from rest_framework.pagination import (
                        LimitOffsetPagination,
                        PageNumberPagination
                                    )

class ProductLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 7


class ProductPageNumberPagination(PageNumberPagination):
    page_size = 4
