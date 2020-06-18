from django_filters import rest_framework as filters
from products.serializers import ProductSerializer, GenreSerializer
from products.models import Product, Genre
from rest_framework import viewsets, mixins

class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('genre_id')

class GenreView(mixins.ListModelMixin,
                viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
