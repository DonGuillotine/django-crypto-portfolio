from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Created Login Test
class LoginTraderTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.user = User.objects.create_user(username='testuser', password='testpassword')