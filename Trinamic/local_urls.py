from django.urls import path

from Trinamic import local_views

app_name = 'Trinamic'
urlpatterns = [
    path('test', local_views.index, name='test')
]
