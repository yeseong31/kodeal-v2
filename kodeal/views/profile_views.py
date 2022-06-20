from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='common:signin')
def index(request):
    """
    마이페이지(프로필)
    """
    return render(request, 'kodeal/profile.html')
