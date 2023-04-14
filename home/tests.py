from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch, MagicMock
from pycoingecko import CoinGeckoAPI

class TestIndexView(TestCase):

    @patch.object(CoinGeckoAPI, 'get_coins_markets')
    def test_index_view(self, mock_get_coins_markets):
        mock_get_coins_markets.return_value = MagicMock()
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        mock_get_coins_markets.assert_called_once_with(vs_currency='usd', order='market_cap_desc', per_page=10)
