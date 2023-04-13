from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


# Created Login Test
class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='testpass')


    #  Test Login with dummy data
    def test_login(self):
        url = reverse('login')
        response = self.client.post(url, {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))


    #  Test Logout with mimic
    def test_logout(self):
        url = reverse('logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))


    # Test for registration success
    def test_registration(self):
            data = {
                'username': 'testuser',
                'password1': 'testpass',
                'password2': 'testpass',
                'email': 'testuser@example.com'
            }
            response = self.client.post(reverse('register'), data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(User.objects.count(), 1)
            user = User.objects.first()
            self.assertEqual(user.username, 'testuser')
            self.assertEqual(user.email, 'testuser@example.com')


    #  Test forgot password
    def test_forgot_password(self):
        url = reverse('password_reset')
        response = self.client.post(url, {
            'email': self.user.email
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('password_reset_done'))