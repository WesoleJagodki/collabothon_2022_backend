from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.http import HttpResponse

from polls.views.user import UserApi, TestAuth


def index(request):
    return HttpResponse("Hello, world. You're at the polls index!!!")


urlpatterns = [
    path("", index, name="index"),
    path("user", UserApi.as_view(), name="index"),
    path("test", TestAuth.as_view(), name="aaindex"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
