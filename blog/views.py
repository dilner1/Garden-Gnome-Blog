from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from.forms import PostForm

# Allows published posts to be displayed on html page

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'open_post.html'

class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'