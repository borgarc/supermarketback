from rest_framework import serializers
from products.models import Product, Genre

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'genre')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields =('id', 'genre')