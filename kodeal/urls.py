from django.urls import path

from kodeal.views import base_views, profile_views, question_views, comment_views

app_name = 'kodeal'

urlpatterns = [
    # ----- base_views.py -----
    # 메인 페이지
    path('', base_views.index, name='index'),
    # 테스트 페이지
    path('test/', base_views.test, name='test'),

    # ----- profile_views.py -----
    # 마이 페이지
    path('profile/', profile_views.index, name='profile'),

    # ----- question_views.py -----
    # QnA 페이지
    path('qna/', question_views.qna, name='qna'),
    # 질문 조회
    path('question/detail/<int:question_id>/', question_views.question_detail, name='question_detail'),
    # 질문 등록
    path('question/create/', question_views.question_create, name='question_create'),

    # ----- comment_views.py -----
    # 코멘트 등록
    path('comment/create/<int:question_id>/', comment_views.comment_create, name='comment_create'),

]