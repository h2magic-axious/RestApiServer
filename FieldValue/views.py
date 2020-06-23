from FieldValue.models import Field, FieldValue
from FieldValue.serializers import FieldSerializer, FieldValueSerializer

from rest_framework import generics
from rest_framework.filters import SearchFilter
from django.http import JsonResponse
from Reference.Pagination import OwnPagination

from Trinamic.models import Category, Item


def whole_fields(request):
    return JsonResponse({'results': [{'id': f.id, 'name': f.name, 'alias': f.alias} for f in Field.objects.all()]})


class FieldList(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'alias']


class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


def whole_field_values(request):
    return JsonResponse(
        {'results': [{'id': fv.id, 'field': fv.field, 'value': fv.value} for fv in FieldValue.objects.all()]})


def whole_field_value_with_item(request, item_id):
    return JsonResponse(
        {'results': [{'id': fv.id, 'field': fv.field, 'value': fv.value} for fv in FieldValue.objects.all() if
                     fv.item_id == item_id]})


def category_fields(request, c_id):
    results = ['型号']
    try:
        category = Category.objects.get(pk=c_id)
        for field in category.fields.split(','):
            if field == '0':
                continue
            results.append(Field.objects.get(pk=int(field)).alias)
    except:
        pass

    return JsonResponse({'results': results})


def category_items(request, c_id):
    category = Category.objects.get(pk=c_id)

    result = []
    for item in category.item_set.all():
        res = {'型号': item.model, 'id': item.id}
        for fv in item.fieldvalue_set.all():
            res[fv.field.alias] = fv.value
        result.append(res)
    return JsonResponse({'results': result})


class FieldValueList(generics.ListCreateAPIView):
    serializer_class = FieldValueSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['value']

    def get_queryset(self):
        queryset = FieldValue.objects.all()

        item_id = self.request.query_params.get('item', None)
        if item_id:
            return queryset.filter(item__id=item_id)

        field_id = self.request.query_params.get('field', None)
        if field_id:
            return queryset.filter(field__id=field_id)

        return queryset


class FieldValueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FieldValue.objects.all()
    serializer_class = FieldValueSerializer


def get_item_all_field_value(request, item_id):
    item = Item.objects.get(pk=item_id)
    results = []
    # 由于 BootstrapVue 没有提供去掉table的thead的方法，这里使用型号作为表头
    for fv in item.fieldvalue_set.all():
        results.append({'型号': fv.field.alias, item.model: fv.value})

    return JsonResponse({'results': results})
