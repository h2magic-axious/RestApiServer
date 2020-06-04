from Media.models import Media
from Media.serializers import MediaSerializer

from rest_framework import generics
from rest_framework.filters import SearchFilter

from Reference.Pagination import OwnPagination


class MediaList(generics.ListCreateAPIView):
    serializer_class = MediaSerializer
    pagination_class = OwnPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'filename']

    def get_queryset(self):
        queryset = Media.objects.all()

        m_type = self.request.query_params.get('media_type', None)
        if m_type:
            return queryset.filter(media_type=m_type)

        item_id = self.request.query_params.get('item', None)
        if item_id:
            return queryset.filter(item__id=item_id)

        return queryset


class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
