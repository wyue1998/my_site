from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, "blog/index.html", {})

def posts(requests):
    pass

def get_post(requests, slug):
    pass