from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag
# import django get_or_404



all_posts = Post.objects.all()

def index(requests):
    latest_posts = all_posts.order_by("-date")[:3]
    return render(
        requests,
        "blog/index.html",
        {
            "posts": latest_posts,
        },
    )

def posts(requests):
    return render(requests, "blog/posts.html", {
        "posts": all_posts.order_by("-date"),
    })


def get_post(requests, slug):
    post = get_object_or_404(all_posts, slug=slug)
    return render(requests, "blog/post_detail.html", {
        'post': post,
        'tags': post.tags.all(),
    })