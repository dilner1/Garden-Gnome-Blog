from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Additional information for Posts in admin dashboard

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    search_fields = ('title', 'content')
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}