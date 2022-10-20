import uuid

from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Advertisement(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False
                          )
    author = models.ForeignKey(get_user_model(),
                               db_column='ad author',
                               on_delete=models.CASCADE,
                               verbose_name=pgettext_lazy('text for Advertisement model', 'Advertisement author'),
                               help_text=_('choose author of advertisement')
                               )
    title = models.CharField(default='',
                             db_column='title',
                             max_length=200,
                             verbose_name=pgettext_lazy('text for Advertisement model', 'Advertisement  title'),
                             help_text=_('enter title of advertisement')
                             )
    date = models.DateField(auto_now_add=True,
                            db_column='date',
                            )
    content_upload = RichTextUploadingField(blank=True,
                                            null=True,
                                            db_column='content_upload',
                                            )

    def __str__(self):
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('ad_detail', args=[str(self.id)])


class Response(models.Model):
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE)

    advertise = models.ForeignKey(Advertisement,
                                  on_delete=models.CASCADE,
                                  related_name='responses',
                                  )
    response = models.TextField(db_column='response_text',
                                max_length=200,
                                verbose_name=pgettext_lazy('text for Response model', 'Response text'),
                                help_text=_('enter text of response')
                                )

    def __str__(self):
        return self.response
