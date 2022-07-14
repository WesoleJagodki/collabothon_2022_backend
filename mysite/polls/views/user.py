from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from marshmallow import Schema, fields
from polls.models import OUserModel
from polls.models import Image


class UserSchema(Schema):
    email = fields.Str(required=True, data_key="Email")
    password = fields.Str(required=True, data_key="Password")
    gender = fields.Str(required=True, data_key="Gender")
    pin = fields.Str(required=True, data_key="PIN")
    username = fields.Str(required=True, data_key="Username")
    birthday = fields.Str(required=True, data_key="BirthDay")


class UserApi(APIView):
    def post(self, request):
        data = UserSchema().load(request.data)
        email = data.pop("email")
        username = data.pop("username")
        password = data.pop("password")
        OUserModel.objects.create_user(username, email, password, **data)
        return Response()

    def get(self, request):
        del request

        a = OUserModel.objects.all()
        return Response(UserSchema().dump(a, many=True))


class TestAuth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)

        a = OUserModel.objects.all()
        return Response(UserSchema().dump(a, many=True))

class LoginImage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        Image(title=request.POST["title"], image=request.FILES["image"], user=request.user).save()

        return Response()