from pybo import views
from django.urls import path, include

app_name = 'pybo'

urlpatterns = [
    # 메인 페이지
    path('', views.index, name='index'),
    # id로 질문 조회
    path('<int:question_id>/', views.detail, name='detail'),
    # 질문 등록
    path('question/create/', views.question_create, name='question_create'),
    # 질문 수정
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # 질문 삭제
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # 답변 등록
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # 답변 수정
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # 답변 삭제
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
]