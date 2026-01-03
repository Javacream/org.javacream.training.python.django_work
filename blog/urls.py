
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("posts/new/", views.post_create, name="post_create"),
    path("posts/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path("ping/", views.PingView.as_view(), name="ping"),
    path("echo/", views.echo, name="echo"),
    path("submit/", views.submit, name="submit"),
]
