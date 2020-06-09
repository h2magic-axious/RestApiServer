from Media.models import Media, MEDIA_TYPES, MEDIA_TAGS
from Media.serializers import MediaSerializer

from rest_framework import generics
from rest_framework.filters import SearchFilter

from Reference.Pagination import OwnPagination

from django.http import JsonResponse


def get_media_type(request):
    return JsonResponse(
        {'count': len(MEDIA_TYPES), 'results': [{'value': value, 'label': label} for value, label in MEDIA_TYPES]})


def whole_media(request):
    return JsonResponse({'results': [{'id': m.id, 'title': m.title} for m in Media.objects.all()]})


class MediaList(generics.ListCreateAPIView):
    serializer_class = MediaSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = Media.objects.all()

        m_type = self.request.query_params.get('media_type', None)
        if m_type:
            return queryset.filter(media_type=m_type)

        m_tag = self.request.query_params.get('tag', None)
        if m_tag:
            return queryset.filter(tag=m_tag)

        item_id = self.request.query_params.get('item', None)
        if item_id:
            return queryset.filter(item__id=item_id)

        return queryset


class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


def get_media_tag(request):
    return JsonResponse(
        {'count': len(MEDIA_TAGS), 'results': [{'value': value, 'label': label} for value, label in MEDIA_TAGS]})
