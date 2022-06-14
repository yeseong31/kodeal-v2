from pybo import views
from django.urls import path, include

app_name = 'pybo'

urlpatterns = [
    # 메인 페이지
    path('', views.index, name='index'),
    # id로 질문 조회
    path('<int:question_id>/', views.detail, name='detail'),
    # 답변 등록
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # 질문 등록
    path('question/create/', views.question_create, name='question_create')
]