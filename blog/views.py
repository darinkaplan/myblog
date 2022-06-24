from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/post_new.html"
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_edit.html"
    fields = ['title', 'author', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("home")
