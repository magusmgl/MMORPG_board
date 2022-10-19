from django.contrib import admin

from .models import Advertisement, Response


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'date')

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'advertise', 'response')
