from .models import Company
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    # Django's Object Relational Mapper
    # System of info exchange between db and Django
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
