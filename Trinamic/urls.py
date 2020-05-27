from django.urls import path

from Trinamic import views

urlpatterns = [
    path('product', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),
    path('category', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),
    path('item', views.ItemList.as_view()),
    path('item/<int:pk>', views.ItemDetail.as_view())
]
