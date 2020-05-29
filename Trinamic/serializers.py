from rest_framework import serializers

from Trinamic.models import Product, Category, Item


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'alias', 'excerpt', 'category_set']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'alias', 'excerpt', 'product', 'item_set']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'model', 'excerpt', 'category']
