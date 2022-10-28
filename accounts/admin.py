from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import OneTimeCode

# Register your models here.

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'is_superuser',
    ]

@admin.register(OneTimeCode)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'code')
    list_display_links = ('user', )
    search_fields = ('user',)
    list_filter = ('user', )

admin.site.register(CustomUser, CustomUserAdmin)
