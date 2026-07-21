from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class LoginTests(APITestCase):
    def test_register_user_creates_active_account(self):
        response = self.client.post(
            reverse('registerUser'),
            {
                'fname': 'Test',
                'lname': 'User',
                'email': 'register@example.com',
                'password': 'register123',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json()['email'] == 'register@example.com')

        user = User.objects.get(email='register@example.com')
        self.assertTrue(user.is_active)

    def test_can_login_with_username(self):
        User = get_user_model()
        User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='admin123',
        )

        response = self.client.post(
            reverse('token_obtain_pair'),
            {'username': 'admin', 'password': 'admin123'},
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)

    def test_can_login_with_email(self):
        User = get_user_model()
        User.objects.create_user(
            username='user@example.com',
            email='user@example.com',
            password='secret123',
        )

        response = self.client.post(
            reverse('token_obtain_pair'),
            {'email': 'user@example.com', 'password': 'secret123'},
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
