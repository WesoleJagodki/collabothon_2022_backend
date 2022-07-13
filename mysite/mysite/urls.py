from django.contrib import admin
from django.urls import include, path
from polls.urls import urlpatterns as polls_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
] + polls_urls

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

