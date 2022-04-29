from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'image', 'content', 'status')
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'value': '',
                    'id': 'formAuth',
                    'type': 'hidden'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Text'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        exclude = ('slug', 'status')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
             'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment'}),
        }
        labels = {
            'body': ''
        }
