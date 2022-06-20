from django.shortcuts import render


def index(request):
    """
    마이페이지(프로필)
    """
    return render(request, 'kodeal/profile.html')
