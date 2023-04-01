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
    username = 'newuser'
    email = 'newuser@mail.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    # --- urls ----
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'signup')
        self.assertNotContains(self.response, 'hi there! something is wrong.')

    def test_signup_form(self):
        newuser = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)



