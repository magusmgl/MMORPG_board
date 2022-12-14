from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='Ivan', email='Ivan@emai.ru', password='testpass123'
        )
        self.assertEqual(user.username, 'Ivan')
        self.assertEqual(user.email, 'Ivan@emai.ru')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin', email='superadmin@emai.ru', password='testpass123'
        )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superadmin@emai.ru')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
