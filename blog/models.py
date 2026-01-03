
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="posts")
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
