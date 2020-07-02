from Trinamic.models import Product, Category, Item
from Trinamic.serializers import ProductSerializer, CategorySerializer, ItemSerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter
from django.http import JsonResponse

from Reference.Pagination import OwnPagination


def whole_products(request):
    return JsonResponse({'results': [{'id': p.id, 'name': p.name, 'alias': p.alias} for p in Product.objects.all()]})


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'alias', 'excerpt']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def whole_categories(request):
    return JsonResponse({'results': [{'id': c.id, 'name': c.name, 'alias': c.alias} for c in Category.objects.all()]})


def whole_categories_with_product(request, p_id):
    return JsonResponse({'results': [{'id': c.id, 'name': c.name, 'alias': c.alias} for c in Category.objects.all() if
                                     c.product_id == p_id]})


class CategoryList(generics.ListCreateAPIView):
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


def whole_items(request):
    return JsonResponse({'results': [{'id': item.id, 'model': item.model} for item in Item.objects.all()]})


def whole_items_with_category(request, c_id):
    return JsonResponse(
        {'results': [{'id': item.id, 'model': item.model} for item in Item.objects.all() if item.category_id == c_id]})


class ItemList(generics.ListCreateAPIView):
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


def seo_product_center(request, p_id):
    category_set = Category.objects.filter(product__id=p_id)
    category_name_list = [c.name for c in category_set]
    items = []
    for c in category_set:
        items.extend([item.model for item in c.item_set.all()])

    return JsonResponse({'content': ','.join(category_name_list + items)})