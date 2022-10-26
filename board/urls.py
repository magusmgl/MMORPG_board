from django.urls import path

from .views import (
    AdsListView,
    UserAdsListView,
    AdDetailView,
    CreateAdView,
    AdUpdateView,
    AdDeleteView,
    ReplaysAdsListView,
)

urlpatterns = [
    path('', AdsListView.as_view(), name='ads_list'),
    path('<uuid:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create_ads/', CreateAdView.as_view(), name='create_ad'),
    path('replays/', ReplaysAdsListView.as_view(), name='replays_list'),
    path('user_ads/', UserAdsListView.as_view(), name='user_ads_list'),
    path('user_ads/<uuid:pk>/edit/', AdUpdateView.as_view(), name='ad_edit'),
    path('user_ads/<uuid:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),

]
