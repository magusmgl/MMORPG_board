from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class BoardPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)
    def test_boardpage_url_name(self):
        responce = self.client.get(reverse('notice_board'))
        self.assertEqual(responce.status_code, 200)