from django.shortcuts import render


from django.http.response import HttpResponse
from polls.models import Image

from django import forms


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Image
        fields = ("title", "image")


def image_upload_view(request):
    Image(title=request.POST["title"], image=request.FILES["image"]).save()

    return HttpResponse()
