from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Advertisement

# Create your views here.
class BoardPageView(ListView):
    model = Advertisement
    template_name = 'board/board.html'
