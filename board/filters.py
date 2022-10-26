import django_filters

from .models import Reply
from django.contrib.auth import get_user_model

class ReplyFilter(django_filters.FilterSet):
    user = get_user_model()
    advertise = django_filters.CharFilter(field_name='advertise__title',
                                          label='advertise title:',
                                          lookup_expr='icontains'
                                          )
    author = django_filters.ModelChoiceFilter(queryset=user.objects.all(),
                                            label = 'author of reply:',
                                        )

    reply = django_filters.CharFilter(field_name='reply',
                                      label='reply text:',
                                      lookup_expr='icontains')

    class Meta:
        model = Reply
        fields = ['advertise', 'author', 'reply']