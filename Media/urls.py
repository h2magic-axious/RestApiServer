from django.urls import path

from Media import views

urlpatterns = [
    path('media', views.MediaList.as_view()),
    path('media/<int:pk>', views.MediaDetail.as_view()),
    path('media/types', views.get_media_type),
    path('media/tags', views.get_media_tag),
    path('media/whole', views.whole_media),
    path('media/whole/item/<int:item_id>', views.whole_media_with_item),
    path('media/<int:item_id>/<str:m_type>/<str:m_tag>', views.get_media)
]
