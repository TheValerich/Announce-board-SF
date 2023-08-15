from django.urls import path
from .views import PostsListView, CommentCreateView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_url'),
    path('comment/', CommentCreateView.as_view(), name='comment_url'),
]
