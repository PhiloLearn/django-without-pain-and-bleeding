from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'