from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):

    def test_home_page_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get("/")
        self.assertContains(response, "Production-Grade Django CI/CD Pipeline")
