from django.urls import path

from .views import BoardPageView

urlpatterns = [
    path('', BoardPageView.as_view(), name='notice_board')
]
