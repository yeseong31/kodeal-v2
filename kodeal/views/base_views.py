from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Kodeal Main Page
    """
    return render(request, 'kodeal/home.html')


@login_required(login_url='common:signin')
def qna(request):
    """
    Kodeal QnA Page
    """
    return render(request, 'kodeal/qna.html')
