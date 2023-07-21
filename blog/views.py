from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, "blog/index.html", {})

def posts(requests):
    return render(requests, "blog/posts.html", {})

def get_post(requests, slug):
    pass