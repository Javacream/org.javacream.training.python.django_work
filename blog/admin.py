
from django.contrib import admin
from django.db.models import Count

from .models import Author, Post, Tag

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "tag_count", "created_at")
    search_fields = ("title", "body", "author__name")
    list_filter = ("created_at", "author")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_tag_count=Count("tags"))

    @admin.display(ordering="author__name")
    def author_name(self, obj):
        return obj.author.name

    @admin.display(ordering="_tag_count")
    def tag_count(self, obj):
        return obj._tag_count
