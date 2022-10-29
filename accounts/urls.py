from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    SignupPageView,
    usual_login_view,
    send_onetime_code,
    login_with_code_view
)

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/entry_code/<int:pk>', login_with_code_view, name='code_entry_page'),
    path('login/send_code', send_onetime_code, name='send_onetime_code'),
    path('login/', usual_login_view, name='login_with_verification_code'),
]
