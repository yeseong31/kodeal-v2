from django.urls import path
from django.views.generic import RedirectView

from kodeal.views import base_views, profile_views, question_views, comment_views, answer_views

app_name = 'kodeal'

urlpatterns = [
    # ----- base_views.py -----
    # 메인 페이지
    path('', base_views.index, name='index'),
    path('home/', RedirectView.as_view(url='/', permanent=True)),
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
    # 질문 삭제
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    # 질문 추천
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # ----- answer_views.py -----
    # 답변 추천
    path('answer/vote/<int:question_id>/', answer_views.answer_vote, name='answer_vote'),

    # ----- comment_views.py -----
    # 코멘트 등록
    path('comment/create/<int:question_id>/', comment_views.comment_create, name='comment_create'),
    # 코멘트 삭제
    path('comment/delete/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),
    # 코멘트 추천
    path('comment/vote/<int:comment_id>/', comment_views.comment_vote, name='comment_vote'),

]