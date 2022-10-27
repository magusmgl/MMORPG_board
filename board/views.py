from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    FormView,
)

from .models import Advertisement, Reply
from .forms import AdvertisementForm, ReplyForm
from .filters import ReplyFilter

class AdsListView(ListView):
    '''Список всех объявлений на  главной странице сайта сайте'''
    model = Advertisement
    ordering = '-date'
    context_object_name = 'ads_list'
    template_name = 'board/ad_list.html'
    paginate_by = 10


class UserAdsListView(ListView):
    model = Advertisement
    ordering = '-date'
    context_object_name = 'ads_list'
    template_name = 'board/ad_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Advertisement.objects.filter(author=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm()
        return context


class AdDetailView(DetailView):
    def get(self, request, *args, **kwargs):
        view = ReplyGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ReplyPost.as_view()
        return view(request, *args, **kwargs)


class ReplyGet(DetailView):
    model = Advertisement
    context_object_name = 'ad'
    template_name = 'board/ad_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReplyForm()
        context['author_rep'] = self.request.user
        return context


class ReplyPost(FormView, LoginRequiredMixin, SingleObjectMixin):
    model = Advertisement
    form_class = ReplyForm
    template_name = 'board/ad_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        reply = form.save(commit=False)
        reply.advertise = self.object
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        ad = self.get_object()
        return reverse('ad_detail', kwargs={'pk': ad.pk})


class CreateAdView(LoginRequiredMixin, CreateView):
    form_class = AdvertisementForm
    context_object_name = 'ad'
    template_name = 'board/ad_create.html'
    raise_exception = True

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'board/ad_create.html'
    context_object_name = 'ad'


class AdDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'board/ad_delete.html'
    success_url = reverse_lazy('ads_list')
    context_object_name = 'ad'


class ReplaysSearchView(ListView):
    model = Reply
    template_name = 'board/replays_list.html'
    context_object_name = 'rep_list'
    paginate_by = 10

    def get_queryset(self):
        queryset = Reply.objects.filter(advertise__author=self.request.user)
        self.filterset = ReplyFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ReplyDeleteView(DeleteView):
    model = Reply
    template_name = 'board/reply_delete.html'
    context_object_name = 'reply'
    success_url = reverse_lazy('replays_list')


def accept_reply(request, pk):
    rep = Reply.objects.get(pk=pk)
    rep.is_accept = True
    rep.save()
    context = {
        'reply': rep
    }
    return render(request, 'board/reply_accept.html', context=context)
