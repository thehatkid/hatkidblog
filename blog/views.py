from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post


class BlogListView(ListView):
    model=Post
    template_name='page_index.html'


class BlogDetailView(DetailView):
    model=Post
    template_name='page_post.html'
