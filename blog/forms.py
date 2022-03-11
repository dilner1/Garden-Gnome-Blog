from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'image', 'content', 'status')
        widget = (
            'title': form.TextInput(attrs={'class': 'form-control'}),
            'slug': form.TextInput(attrs={'class': 'form-control'}),
            'author': form.Select(attrs={'class': 'form-control'}),
            'image': form.TextInput(attrs={'class': 'form-control'}),
            'content': form.Textarea(attrs={'class': 'form-control'}),
            'status': form.Select(attrs={'class': 'form-control'}),
        )