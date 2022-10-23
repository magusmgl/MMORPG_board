from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from .views import AdsListView, AdDetailView
from .models import Advertisement


# Create your tests here.
class BoardTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User = get_user_model()
        user = User.objects.create_user(username='testuser',
                                        first_name='testuser_name',
                                        last_name='testuser_last_name',
                                        email='testuser@emai.ru',
                                        password='testpass123',
                                        )
        cls.ad = Advertisement.objects.create(
            author=user,
            title='some title',
            content_upload='<h1>some content<h1>'
        )

    def test_ad_listing(self):
        self.assertEqual(f'{self.ad.author}', 'testuser')
        self.assertEqual(f'{self.ad.title}', 'some title')
        self.assertEqual(f'{self.ad.content_upload}', '<h1>some content<h1>')

    def test_ad_list_view(self):
        view = resolve('/')
        response = self.client.get(reverse('ads_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/ad_list.html')
        self.assertContains(response, 'Ads board')
        self.assertEqual(view.func.__name__, AdsListView.as_view().__name__)

    def test_ad_detail_view(self):
        response = self.client.get(self.ad.get_absolute_url())
        no_response = self.client.get('/ad/232313')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'board/ad_detail.html')
        self.assertContains(response, '<h1>some content<h1>')
