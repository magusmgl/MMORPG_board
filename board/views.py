from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .models import Advertisement
from .forms import AdvertisementForm


# Create your views here.
class AdsListView(ListView):
    model = Advertisement
    ordering = '-date'
    context_object_name = 'ads_list'
    template_name = 'board/ad_list.html'
    paginate_by = 10


class UserAdsListVies(ListView):
    model = Advertisement
    ordering = '-date'
    context_object_name = 'ads_list'
    template_name = 'board/ad_list.html'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Advertisement.objects.filter(author=user)


class AdDetailView(DetailView):
    model = Advertisement
    context_object_name = 'ad'
    template_name = 'board/ad_detail.html'


class CreateAdView(CreateView):
    form_class = AdvertisementForm
    context_object_name = 'ad'
    template_name = 'board/ad_create.html'

    def form_valid(self, form):
        form.instance.author=self.request.user
        # ad = form.save(commit=False)
        # ad.author = self.request.user
        # ad.save()
        return super().form_valid(form)

class AdUpdateView(UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'board/ad_create.html'
    context_object_name = 'ad'


class AdDeleteView(DeleteView):
    model = Advertisement
    template_name = 'board/ad_delete.html'
    success_url = reverse_lazy('ads_list')
    context_object_name = 'ad'


