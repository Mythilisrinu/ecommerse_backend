from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .utils import generate_token


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

    def test_activate_account_view_accepts_uidb64(self):
        user = User.objects.create_user(
            username='activate-user',
            email='activate@example.com',
            password='secret123',
            is_active=False,
        )
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        token = generate_token.make_token(user)

        response = self.client.get(reverse('active', kwargs={'uidb64': uidb64, 'token': token}))

        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertTrue(user.is_active)
