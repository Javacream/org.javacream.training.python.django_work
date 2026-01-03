
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

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
