from django.urls import path
from MyUser import views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('user', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('api-token', auth_views.obtain_auth_token)
]
