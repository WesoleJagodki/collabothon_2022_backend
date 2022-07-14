from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.http import HttpResponse

from polls.views.user import UserApi, TestAuth, LoginImage
from polls.views.image import image_upload_view


def index(request):
    return HttpResponse("Hello, world. You're at the polls index!!!")


urlpatterns = [
    path("api/", index, name="index"),
    path("api/user", UserApi.as_view(), name="index"),
    path("api/test", TestAuth.as_view(), name="aaindex"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/upload", LoginImage.as_view(), name="image"),

]
