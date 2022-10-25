from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Advertisement, Reply


class AdvertisementForm(forms.ModelForm):
    content_upload = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Advertisement
        fields = ['category', 'title', 'content_upload']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply', ]
        widgets = {
            'reply': forms.Textarea(attrs={'cols': 5, 'rows': 2}),
        }
