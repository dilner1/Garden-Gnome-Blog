from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'image', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your post title here'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is the link to your post'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }