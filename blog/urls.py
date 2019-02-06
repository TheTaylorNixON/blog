from django.urls import path

from .views import *


urlpatterns = [
    path('post/', PostsList.as_view(), name='posts_list_url'),
    path('tags/', TagsList.as_view(), name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='tag_detail_url')
]