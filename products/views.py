from products.serializers import ProductSerializer
from products.models import Product
from rest_framework import viewsets

class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
