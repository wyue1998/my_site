from datetime import date
from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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


# class GetPostView(DetailView): # DetailView automatically retrieves the object based on slug
#     model = Post
#     template_name = "blog/post_detail.html"
#     # context_object_name = "post" # DetailView automatically calls object Model.lower() as context_object_name

#     def get_context_data(self, **kwargs: Any):
#         context = super().get_context_data(**kwargs)
#         context['tags'] = self.object.tags.all()
#         context['comment_form'] = CommentForm()
#         return context
    
class GetPostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            'post': post,
            'tags': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by("-id"),
        }
        return render(request, 'blog/post_detail.html', context=context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = Post.objects.get(slug=slug)
            comment.save()
            return HttpResponseRedirect(request.path)
        else:
            post = Post.objects.get(slug=slug)
            context = {
                'post': post,
                'tags': post.tags.all(),
                'comment_form': CommentForm(),
                'comments': post.comments.all().order_by("-id"),
            }
            return render(request, 'blog/post_detail.html', context=context)



class AddInfoView(CreateView):
    template_name = "blog/add_info.html"
    model = Post
    fields = ['upload_image']
    success_url = "/posts/"

class ReadLaterView(View):
    def get(self, request):
        print(request.session.get('stored_posts', []))
        stored_posts = request.session.get('stored_posts', [])
        posts = Post.objects.filter(id__in=stored_posts) # __in is a lookup that allows us to filter based on a list of values
        context = {
            'posts': posts,
        }
        return render(request, 'blog/stored_posts.html', context=context)
    
    def post(self, request):
        stored_posts = request.session.get('stored_posts', [])
        post_id = int(request.POST['post_id'])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session['stored_posts'] = stored_posts # If the request session is not updated with this line, the session database will not be saved.
            print(stored_posts)
            return HttpResponseRedirect("/posts/")
        print('This post is already in your read later list')
        return HttpResponseRedirect("/posts/")