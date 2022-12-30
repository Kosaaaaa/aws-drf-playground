from unittest.mock import patch
from urllib.parse import urlencode, urlparse

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.views import JOKES_CATEGORIES, JOKES_LANGUAGES


def add_url_query_params(url: str, additional_params: dict) -> str:
    url_components = urlparse(url)
    merged_params = additional_params
    updated_query = urlencode(merged_params)
    return url_components._replace(query=updated_query).geturl()


class JokesApiTestCase(APITestCase):
    url = reverse('core:jokes')

    def test_without_params(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('jokes', response.json())

    @patch('core.views.pyjokes.get_jokes')
    def test_with_valid_params(self, mocked_get_jokes):
        language = JOKES_LANGUAGES[1]
        category = JOKES_CATEGORIES[1]

        jokes = ['joke1', 'joke2']
        mocked_get_jokes.return_value = jokes
        response = self.client.get(add_url_query_params(self.url, {'language': language, 'category': category}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('jokes', response.json())

        self.assertEqual(response.json()['jokes'], jokes)

    def test_with_invalid_params(self):
        response = self.client.get(add_url_query_params(self.url, {'language': 'p0p0p0', 'category': 'qwerty'}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
