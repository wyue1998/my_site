from datetime import date
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

all_posts = Post.objects.all()

class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset().order_by("-date")[:3]
        return queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["posts"] = all_posts.order_by("-date")[:3]
    #     return context


class PostsView(ListView):
    template_name = "blog/posts.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        return super().get_queryset().order_by("-date")


class GetPostView(DetailView): # DetailView automatically retrieves the object based on slug
    model = Post
    template_name = "blog/post_detail.html"
    # context_object_name = "post" # DetailView automatically calls object Model.lower() as context_object_name

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        return context

class AddInfoView(CreateView):
    template_name = "blog/add_info.html"
    model = Post
    fields = ['upload_image']
    success_url = "/posts/"