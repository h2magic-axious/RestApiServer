from django.urls import path
from MyUser import views
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('user', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('token', views.get_user),
    path('refresh', refresh_jwt_token)
]
