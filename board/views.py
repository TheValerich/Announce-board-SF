from django.views.generic import CreateView, ListView, UpdateView
from .models import Post, Comment


class PostsListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'
    fields = [
        'content',
    ]
