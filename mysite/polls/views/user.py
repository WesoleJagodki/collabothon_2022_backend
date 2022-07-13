from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from marshmallow import Schema, fields
from polls.models import OUserModel


class UserSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)


class UserApi(APIView):
    def post(self, request):
        data = UserSchema().load(request.data)
        email = data.pop("email")
        OUserModel.objects.create_user(email, email, data.pop("password"), **data)
        return Response()

    def get(self, request):
        del request

        a = OUserModel.objects.all()
        return Response(UserSchema().dump(a, many=True))


class TestAuth(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        del request

        a = OUserModel.objects.all()
        return Response(UserSchema().dump(a, many=True))
