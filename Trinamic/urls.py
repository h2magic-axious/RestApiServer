from django.urls import path

from Trinamic import views

urlpatterns = [
    path('product', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),
    path('product/whole', views.whole_products),
    path('product/seo/<int:p_id>', views.seo_product_center),
    path('category', views.CategoryList.as_view()),
    path('category/<int:pk>', views.CategoryDetail.as_view()),
    path('category/whole', views.whole_categories),
    path('category/whole/<int:p_id>', views.whole_categories_with_product),
    path('item', views.ItemList.as_view()),
    path('item/<int:pk>', views.ItemDetail.as_view()),
    path('item/whole', views.whole_items),
    path('item/whole/<int:c_id>', views.whole_items_with_category),
]
