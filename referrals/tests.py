from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Referral

class ReferralLinkTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_referral_link_generation(self):
        # Ensure that a referral link is generated for the currently logged-in user
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('referral_link'))
        referral = Referral.objects.get(referrer=self.user)
        referral_link = response.context['referral_link']
        self.assertEqual(referral_link, f'http://testserver{reverse("register")}?ref={referral.referral_code}')
