from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Advertisement


class AdvertisementForm(forms.ModelForm):
    content_upload = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Advertisement
        fields = ['category', 'title', 'content_upload']
