from django.contrib.auth.models import AbstractUser, User, UserManager
from django.db import models
from django.db.models.expressions import fields

# Create your models here.


class OUserModel(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={"unique": "An owner with that email already exists."},
    )
    first_name = models.TextField()
    last_name = models.TextField()
    password = models.TextField()

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: list = []
