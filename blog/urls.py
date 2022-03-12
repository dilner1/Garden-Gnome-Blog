from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='open_post'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('post/<slug:slug>/edit', views.UpdatePost.as_view(), name='edit_post'),
]