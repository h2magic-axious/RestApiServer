from django.urls import path

from FieldValue import views

urlpatterns = [
    path('field', views.FieldList.as_view()),
    path('field/<int:pk>', views.FieldDetail.as_view()),
    path('field/whole', views.whole_fields),
    path('fieldvalue', views.FieldValueList.as_view()),
    path('fieldvalue/<int:pk>', views.FieldValueDetail.as_view()),
    path('fieldvalue/whole', views.whole_field_values)
]
