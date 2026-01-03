
from django.test import TestCase
from django.urls import reverse

from .models import Author, Post

class PostModelTests(TestCase):
    def test_str_returns_title(self):
        a = Author.objects.create(name="Ada", email="ada@example.com")
        p = Post.objects.create(author=a, title="Hello World", body="Body")
        self.assertEqual(str(p), "Hello World")

class PingViewTests(TestCase):
    def test_ping_returns_ok(self):
        resp = self.client.get(reverse("ping"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"status": "ok"})

class AuthRedirectTests(TestCase):
    def test_post_create_requires_login(self):
        resp = self.client.get(reverse("post_create"))
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/accounts/login/", resp["Location"])
