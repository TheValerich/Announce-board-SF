from django.urls import path
from .views import PostsListView, CommentCreateView, PostDetailView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_url'),
    path('comment/', CommentCreateView.as_view(), name='comment_url'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_url'),
]
