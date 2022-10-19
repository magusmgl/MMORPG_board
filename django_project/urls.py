from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    # Managment user
    # path('accounts/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Local apps
    path('', include('board.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
