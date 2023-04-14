from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class HoldingsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )

    def test_holdings_view_with_authenticated_user(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpass')

        # Make a GET request to the holdings view
        response = self.client.get(reverse('holdings'))

        # Check that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the expected data
        self.assertContains(response, 'BTC')
        self.assertContains(response, 'ETH')
        self.assertContains(response, 'FG')

        # Log out the user
        self.client.logout()

    def test_holdings_view_with_unauthenticated_user(self):
        # Make a GET request to the holdings view
        response = self.client.get(reverse('holdings'))

        # Check that the response status code is 302 FOUND
        self.assertEqual(response.status_code, 302)

        # Check that the response redirects to the login page
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('holdings'))
