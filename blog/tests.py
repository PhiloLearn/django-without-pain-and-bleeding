from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(title="first post", description="this is firt", status=True)
    
    def test_post_list(self):
        self.assertEqual(f"{self.post.title}", "first post")
        self.assertEqual(f"{self.post.description}", "this is firt")
        self.assertEqual(self.post.status, True)

    def test_post_list_view(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'first post')
        self.assertTemplateUsed(response, 'blog/blog_list.html')

    def test_post_detail_view(self):
        response = self.client.get(self.post.get_absolute_url())
        no_response = self.client.get('blog/42')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'first post')
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
