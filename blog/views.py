from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import redirect
from .models import Post
from .models import Comment
from .forms import CommentForm


class BlogListView(ListView):
    model = Post
    template_name = 'page_index.html'


class BlogDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'page_post.html'
    form_class = CommentForm
    
    def get_context_data(self, **kwargs):
        data = super(BlogDetailView, self).get_context_data(**kwargs)
        comments = Comment.objects.filter(
            post=self.get_object()
        ).order_by('-created_at')
        data['comments'] = comments
        data['comment_form'] = CommentForm()
        return data
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('post', self.kwargs['pk'])
        
        comment = Comment(
            post=self.get_object(),
            author=self.request.user,
            content=form.cleaned_data.get('content')
        )
        comment.save()
        return redirect('post', self.kwargs['pk'])
    
    def form_invalid(self, form):
        return redirect('post', self.kwargs['pk'])
