from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView

# Create your tests here.

class HomePageTest(SimpleTestCase):
    # --- setUp ---
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    # --- urls ----
    def test_homepage_url_exist_at_correct_loacation(self):
        self.assertEqual(self.response.status_code, 200)

    # --- templates ---
    def test_homepage_template_used(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'home page')
    
    def test_homepage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'hi there! something is wrong.')

    # --- view ---
    def test_homepage_url_resolve_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)