from django.urls import path

from Media import views

urlpatterns = [
    path('media', views.MediaList.as_view()),
    path('media/<int:pk>', views.MediaDetail.as_view()),
    path('media/types', views.get_media_type),
    path('media/tags', views.get_media_tag),
    path('media/whole', views.whole_media)
]
