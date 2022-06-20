from django.urls import path

from kodeal.views import base_views, profile_views

app_name = 'kodeal'

urlpatterns = [
    # ----- base_views.py -----
    # 메인 페이지
    path('', base_views.index, name='index'),
    # QnA 메인 페이지
    path('qna/', base_views.qna, name='qna'),

    # --- profile_views.py ---
    # 마이 페이지
    path('profile/', profile_views.index, name='profile'),

]