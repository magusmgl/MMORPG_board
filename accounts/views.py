import random

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from allauth.account.forms import LoginForm

from .forms import CustomUserCreationForm, EnterOnetimeCodeForm
from .models import OneTimeCode


class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


def usual_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user_login = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=user_login, password=password)
        if user is not None:
            OneTimeCode.objects.create(user=user, code=random.randint(12345, 32767))
            return redirect('send_onetime_code')
        else:
            form.add_error(None, "User was not found (check your username and password)")
    else:
        form = LoginForm()
    return render(request, template_name='accounts/login.html', context={'form': form})


def login_with_code_view(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.method == 'POST':
        form = EnterOnetimeCodeForm(request.POST)
        code = request.POST['code']
        if OneTimeCode.objects.filter(code=code, user=user).exists():
            login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')
            return redirect('ads_list')
        else:
            form.add_error(None, 'Login verification code is incorrect')
    else:
        form = EnterOnetimeCodeForm()
    return render(request, template_name='accounts/enter_onetime_code.html',
                  context={'form': form, 'username': user.username})


def send_onetime_code(request):
    return render(request, template_name='accounts/send_onetime_code.html')
