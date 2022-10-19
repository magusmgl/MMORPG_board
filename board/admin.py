from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from .models import Advertisement, Response


class AdvertisementAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget)
    class Meta:
        model = Advertisement
        fields = ('author', 'title', 'content_upload')


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    form = AdvertisementAdminForm
    list_display = ('author', 'title', 'content_upload')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'advertise', 'response')
