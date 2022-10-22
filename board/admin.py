from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from .models import Advertisement, Response


class AdvertisementAdminForm(forms.ModelForm):
    content_upload = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = Advertisement
        fields = ('author', 'title', 'category', 'content_upload')


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    form = AdvertisementAdminForm
    list_display = ('id', 'author', 'title', 'date', 'category', 'content_upload')
    list_display_links = ('author', 'title')
    search_fields = ('author', 'title', 'date')
    list_filter = ('author', 'category')


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'advertise', 'response')
