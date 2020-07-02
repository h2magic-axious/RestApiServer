from django.urls import path

from Trinamic import local_views

app_name = 'Trinamic'
urlpatterns = [
    path('test', local_views.index, name='test'),
    path('product-center/<int:p_id>/<int:c_id>', local_views.product_center, name='product-center'),
    path('item-detail/<int:item_id>', local_views.item_detail, name='item-detail')
]
