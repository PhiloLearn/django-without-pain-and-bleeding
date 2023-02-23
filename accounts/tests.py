from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .views import SignupView
from .forms import CustomUserCreationForm

# Create your tests here.

class CustomeUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='leo', email='leo@email.com', password='testpass123'
        )
        self.assertEqual(user.username, 'leo')
        self.assertEqual(user.email, 'leo@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin', email='superadmin@email.com', password='testpass123'
        )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    # --- urls ----
    def test_signup_url_exist_at_correct_loacation(self):
        self.assertEqual(self.response.status_code, 200)

    # --- templates ---
    def test_signup_template_used(self):
        self.assertTemplateUsed(self.response, 'registration/signup.html')

    def test_signup_contains_correct_html(self):
        self.assertContains(self.response, 'signup')
    
    def test_singup_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'hi there! something is wrong.')

    # --- form ---
    def test_singup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    # --- view ---
    def test_singup_url_resolve_signupview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, SignupView.as_view().__name__)


