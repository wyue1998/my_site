from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts/", views.PostsView.as_view(), name="posts"),
    path("posts/<slug:slug>/", views.GetPostView.as_view(), name="get_post"),
    # path("add_info/", views.AddInfoView.as_view(), name="add_info"),
    path("read-later", views.ReadLaterView.as_view(), name="read_later"),
]
