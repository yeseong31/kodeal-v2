from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photo': photos})
