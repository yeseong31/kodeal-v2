from django.shortcuts import render


def index(request):
    """
    Kodeal Main Page
    """
    return render(request, 'kodeal/home.html')
