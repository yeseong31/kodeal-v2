from pybo import views
from django.urls import path

from .views import base_views, question_views, answer_views

app_name = 'pybo'

urlpatterns = [
    # ----- base_views.py -----
    # 메인 페이지
    path('', base_views.index, name='index'),
    # id로 질문 조회
    path('<int:question_id>/', base_views.detail, name='detail'),

    # ----- question_views.py -----
    # 질문 등록
    path('question/create/', question_views.question_create, name='question_create'),
    # 질문 수정
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    # 질문 삭제
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    # 질문 추천
    path('question/vote/<int:question_id>/', question_views.question_vote, name='question_vote'),

    # ----- answer_views.py -----
    # 답변 등록
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    # 답변 수정
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    # 답변 삭제
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    # 답변 추천
    path('answer/vote/<int:answer_id>/', answer_views.answer_vote, name='answer_vote'),
]