"""ChiplinksWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework_jwt.views import ObtainJSONWebToken

from Reference.Searcher import search

RESTFUL_URL = 'api/private/v1/'

urlpatterns = [
    path(RESTFUL_URL + 'login', ObtainJSONWebToken.as_view()),
    path(RESTFUL_URL, include('Trinamic.urls')),
    path(RESTFUL_URL, include('MyUser.urls')),
    path(RESTFUL_URL, include('FieldValue.urls')),
    path(RESTFUL_URL, include('Media.urls')),
    path(RESTFUL_URL, include('Resource.urls')),
    path(RESTFUL_URL, include('Blog.urls')),
    path('api/search/<str:query>', search)
]
