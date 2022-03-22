from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from .forms import PostForm, CommentForm

# Allows published posts to be displayed on html page

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(approved=True)
        new_comment = None

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.isValid():

                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()

            else:
                comment_form = CommentForm()
                return render(request, 'open_post.html', 
                {'post': post,
                'comments': comments,
                'new_comment': new_comment,
                'comment_form': comment_form
                })

    
class AddPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'edit_post.html'
    field = ['title', 'image', 'content', 'status']