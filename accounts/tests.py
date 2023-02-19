from django.test import TestCase
from django.contrib.auth import get_user_model

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