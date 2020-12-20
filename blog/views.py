from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Post
from .models import Comment
from .forms import CommentForm


class BlogListView(ListView):
    model = Post
    template_name = 'page_index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'page_post.html'
    
    def get_context_data(self, **kwargs):
        data = super(BlogDetailView, self).get_context_data(**kwargs)
        comments = Comment.objects.filter(post=self.get_object()).order_by('-created_at')
        data['comments'] = comments
        data['comment_form'] = CommentForm()
        return data
    
    def post(self, request, *args, **kwargs):
        # TODO: prevent comment duplication after reloading page. (CSRF?)
        comment = Comment(
            content=request.POST.get('content'),
            author=self.request.user,
            post=self.get_object()
        )
        comment.save()
        return self.get(self, request, *args, **kwargs)
