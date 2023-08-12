from django.views.generic import CreateView, ListView, UpdateView
from .models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
