from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class BoardPageView(TemplateView):
    template_name = 'board.html'
