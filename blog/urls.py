
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ping/", views.PingView.as_view(), name="ping"),
    path("echo/", views.echo, name="echo"),
    path("submit/", views.submit, name="submit"),
]
