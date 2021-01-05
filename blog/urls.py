from django.urls import path
from .views import PostListView, post_detail, SearchPostList

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', PostListView.as_view(), name='post_list_by_tag'),
    path('posts/search/', SearchPostList.as_view(), name='search_post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail, name='post_detail'),
]
