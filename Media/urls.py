from django.urls import path

from Media import views

urlpatterns = [
    path('media', views.MediaList.as_view()),
    path('media/<int:pk>', views.MediaDetail.as_view())
]
