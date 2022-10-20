from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Advertisement


# Create your views here.
class AdListView(ListView):
    model = Advertisement
    context_object_name = 'ad_list'
    template_name = 'board/ad_list.html'


class AdDetailView(DetailView):
    model = Advertisement
    context_object_name = 'ad'
    template_name = 'board/ad_detail.html'
