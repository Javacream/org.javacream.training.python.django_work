
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Post

def api_posts(request):
    page = int(request.GET.get("page", 1))
    size = int(request.GET.get("size", 10))

    qs = Post.objects.select_related("author").prefetch_related("tags").order_by("-created_at")
    paginator = Paginator(qs, size)
    page_obj = paginator.get_page(page)

    items = []
    for p in page_obj.object_list:
        items.append({
            "id": p.id,
            "title": p.title,
            "author": p.author.name,
            "tags": [t.name for t in p.tags.all()],
            "created_at": p.created_at.isoformat(),
        })

    return JsonResponse({
        "page": page_obj.number,
        "size": size,
        "pages": paginator.num_pages,
        "count": paginator.count,
        "items": items,
    })

def api_post_detail(request, pk: int):
    p = get_object_or_404(
        Post.objects.select_related("author").prefetch_related("tags"),
        pk=pk
    )
    return JsonResponse({
        "id": p.id,
        "title": p.title,
        "body": p.body,
        "author": {"name": p.author.name, "email": p.author.email},
        "tags": [t.name for t in p.tags.all()],
        "created_at": p.created_at.isoformat(),
    })
