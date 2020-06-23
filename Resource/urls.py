from django.urls import path

from Resource import views

urlpatterns = [
    path('res/type', views.ResourceTypeList.as_view()),
    path('res/type/<int:pk>', views.ResourceTypeDetail.as_view()),
    path('res/type/whole', views.whole_resource_type),
    path('res/content', views.ResourceContentList.as_view()),
    path('res/content/<int:pk>', views.ResourceContentDetail.as_view()),
    path('res/content/whole', views.whole_resource_content),
    path('res/content/whole/item/<int:item_id>', views.whole_resource_content_with_item)
]
