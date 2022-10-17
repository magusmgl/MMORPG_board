from django.test import TestCase
from django.urls import reverse, resolve

from .views import BoardPageView


# Create your tests here.
class BoardPageTest(TestCase):
    def setUp(self) -> None:
        url = reverse('notice_board')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_boardpage_template(self):
        self.assertTemplateUsed(self.response, 'board.html')

    # def test_boardpage_contains_correct_html(self):
    #     self.assertContains(self.response, 'notice board')

    def test_boardpage_url_resolves_boardpageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, BoardPageView.as_view().__name__)