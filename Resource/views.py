from Resource.models import ResourceType, ResourceContent
from Resource.serializers import ResourceTypeSerializer, ResourceContentSerializer

from rest_framework import generics
from rest_framework.filters import SearchFilter
from django.http import JsonResponse

from Trinamic.models import Item

from Reference.Pagination import OwnPagination


def whole_resource_type(request):
    return JsonResponse(
        {'results': [{'id': rt.id, 'name': rt.name, 'alias': rt.alias} for rt in ResourceType.objects.all()]})


class ResourceTypeList(generics.ListCreateAPIView):
    serializer_class = ResourceTypeSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'alias']
    queryset = ResourceType.objects.all()


class ResourceTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer


def whole_resource_content(request):
    return JsonResponse({
        'results': [{'id': rc.id, 'name': rc.name} for rc in ResourceContent.objects.all()]
    })


def whole_resource_content_with_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    resource_list = item.resourcecontent_set.all()

    type_list = set([res.resource_type.alias for res in resource_list])
    results = {tl: [] for tl in type_list}
    for res in resource_list:
        results[res.resource_type.alias].append({
            'id': res.id,
            'name': res.name,
            'url': res.using_url
        })

    return JsonResponse({'results': results, 'keys': list(type_list)})


class ResourceContentList(generics.ListCreateAPIView):
    serializer_class = ResourceContentSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = ResourceContent.objects.all()

        m_type = self.request.query_params.get('resource_type', None)
        if m_type:
            return queryset.filter(resource_type=m_type)

        item_id = self.request.query_params.get('item', None)
        if item_id:
            return queryset.filter(item__id=item_id)

        return queryset


class ResourceContentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResourceContentSerializer
    queryset = ResourceContent.objects.all()
