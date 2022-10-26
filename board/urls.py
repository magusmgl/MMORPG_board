from django.urls import path

from .views import (
    AdsListView,
    UserAdsListView,
    AdDetailView,
    CreateAdView,
    AdUpdateView,
    AdDeleteView,
    ReplaysSearchView,
    ReplyDeleteView,
    accept_reply,
)

urlpatterns = [
    path('', AdsListView.as_view(), name='ads_list'),
    path('<uuid:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create_ads/', CreateAdView.as_view(), name='create_ad'),
    path('user_ads/', UserAdsListView.as_view(), name='user_ads_list'),
    path('user_ads/<uuid:pk>/edit/', AdUpdateView.as_view(), name='ad_edit'),
    path('user_ads/<uuid:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('replays/', ReplaysSearchView.as_view(), name='replays_list'),
    path('replays/<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply_delete'),
    path('replays/<int:pk>/accept/', accept_reply, name='reply_accept'),
]
