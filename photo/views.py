from django.shortcuts import render, get_object_or_404, redirect

from .forms import PhotoForm
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/photo_list.html', {'photos': photos})


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'photo/photo_detail.html', {'photo': photo})


def photo_post(request):
    if request.method == 'POST':
        # POST로 받아온 내용으로 form 구성
        form = PhotoForm(request.POST)
        # form이 유효한 경우 db에 데이터 저장
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo:photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
    return render(request, 'photo/photo_post.html', {'form': form})


def photo_edit(request, pk):
    # 기존의 내용으로 구성하기 위해 데이터 존재 여부를 먼저 확인
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo:photo_detail', pk=photo.pk)
    else:
        # '등록' 과정과는 다른 부분... 기존의 내용으로 form 구성 후 화면에 출력
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form': form})
