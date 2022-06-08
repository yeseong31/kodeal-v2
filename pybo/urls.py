from pybo import views
from django.urls import path, include

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
]