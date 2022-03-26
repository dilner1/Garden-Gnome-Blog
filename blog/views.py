from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        template_name = 'open_post.html'
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        new_comment = None
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = postnew_comment.save()
        else:
            comment_form = CommentForm()
        return render(request, template_name,{'post':post,
        'comments':comments,
        'new_comment': new_comment,
        'comment_form': comment_form}) 
        
class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    field = ['title', 'image', 'content', 'status']

class DeleteView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')