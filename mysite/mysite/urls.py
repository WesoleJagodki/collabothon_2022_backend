from django.contrib import admin
from django.urls import include, path
from polls.urls import urlpatterns as polls_urls

urlpatterns = [
    path("admin/", admin.site.urls),
] + polls_urls
