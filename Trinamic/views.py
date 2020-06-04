from Trinamic.models import Product, Category, Item
from Trinamic.serializers import ProductSerializer, CategorySerializer, ItemSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter

from Reference.Pagination import OwnPagination

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'alias', 'excerpt']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryList(generics.ListCreateAPIView):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'alias', 'excerpt']

    def get_queryset(self):
        queryset = Category.objects.all()

        product_id = self.request.query_params.get('product', None)
        if product_id:
            queryset = queryset.filter(product__id=product_id)

        return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemList(generics.ListCreateAPIView):
    # queryset = Item.objects.all()
    serializer_class = ItemSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['model', 'excerpt']

    def get_queryset(self):
        queryset = Item.objects.all()

        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
