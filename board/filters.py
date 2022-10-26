import django_filters

from .models import Reply, Advertisement
from django.contrib.auth import get_user_model


class ReplyFilter(django_filters.FilterSet):
    advertise = django_filters.CharFilter(field_name='advertise__title',
                                          label='advertise title:',
                                          lookup_expr='icontains'
                                          )
    user = get_user_model()
    author = django_filters.ModelChoiceFilter(queryset=user.objects.all(),
                                              label='author of reply:',
                                              empty_label='author is not select'
                                              )

    reply = django_filters.CharFilter(field_name='reply',
                                      label='reply text:',
                                      lookup_expr='icontains')

    class Meta:
        model = Reply
        fields = ['advertise', 'author', 'reply']
