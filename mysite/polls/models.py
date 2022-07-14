from django.contrib.auth.models import AbstractUser, User, UserManager
from django.db import models
from django.db.models.expressions import fields

# Create your models here.


class OUserModel(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={"unique": "An owner with that email already exists."},
    )
    password = models.TextField()
    gender = models.TextField()
    pin = models.TextField()
    username = models.TextField(unique=True)
    birthday = models.TextField()

    USERNAME_FIELD: str = "username"
    REQUIRED_FIELDS: list = []


class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title
