from django.shortcuts import render

from django.http.response import HttpResponse

def image_upload_view(request):
    """Process images uploaded by users"""
    print(request.FILES)
    return HttpResponse()


