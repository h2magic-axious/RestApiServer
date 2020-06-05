from FieldValue.models import Field, FieldValue
from FieldValue.serializers import FieldSerializer, FieldValueSerializer

from rest_framework import generics
from rest_framework.filters import SearchFilter
from django.http import JsonResponse
from Reference.Pagination import OwnPagination


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
