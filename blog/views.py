
import logging
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from .forms import PostForm
from .models import Post

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

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            logger.info("Post created: id=%s title=%s", post.id, post.title)
            return redirect(reverse("home"))
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})

@staff_member_required
def post_delete(request, pk: int):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        logger.warning("Post deleted: id=%s title=%s", post.id, post.title)
        post.delete()
        return redirect(reverse("home"))
    return render(request, "blog/post_confirm_delete.html", {"post": post})
