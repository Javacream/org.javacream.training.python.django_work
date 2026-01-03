
import logging
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .forms import PostForm

logger = logging.getLogger(__name__)

def home(request):
    return render(request, "blog/home.html")

def about(request):
    return render(request, "blog/about.html")

class PingView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})

def echo(request):
    msg = request.GET.get("msg", "")
    return JsonResponse({"echo": msg})

def submit(request):
    if request.method != "POST":
        return JsonResponse({"detail": "Method not allowed"}, status=405)
    name = request.POST.get("name", "")
    return JsonResponse({"received": name})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            logger.info("Post created: id=%s title=%s", post.id, post.title)
            return redirect(reverse("home"))  # PRG
    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})
