from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
