
from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("posts/new/", views.post_create, name="post_create"),
    path("posts/<int:pk>/delete/", views.post_delete, name="post_delete"),

    path("api/posts/", views_api.api_posts, name="api_posts"),
    path("api/posts/<int:pk>/", views_api.api_post_detail, name="api_post_detail"),

    path("ping/", views.PingView.as_view(), name="ping"),
    path("echo/", views.echo, name="echo"),
    path("submit/", views.submit, name="submit"),
]
