from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('', views.api_root),
    path('blog/',
         views.BlogList.as_view(),
         name='blog-list'),
    path('blog/<int:pk>/',
         views.BlogDetail.as_view(),
         name='blog-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail'),
    path('blog/<int:pk>/highlight/',
         views.BlogHighlight.as_view(),
         name='blog-highlight'),
]

urlpatterns = format_suffix_patterns(urlpatterns)