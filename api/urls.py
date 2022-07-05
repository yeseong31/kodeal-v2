from django.urls import path

from api.views.auth_view import CheckIDView, CheckEmailView, UserActivateView, SignupView, SigninView

app_name = 'api'

urlpatterns = [
    # ----- Authentication -----
    # 회원 가입
    path('signup/', SignupView.as_view()),
    # 로그인
    path('signin/', SigninView.as_view()),
    # 아이디 중복 확인
    path('signup/check/id/', CheckIDView.as_view()),
    # 이메일 인증 링크 전송
    path('signup/check/email/', CheckEmailView.as_view()),
    # 이메일 유효성 검증
    path('activate/<str:uidb64>/<str:token>/', UserActivateView.as_view()),

    # ----- QnA -----
    # path('qna/<int:pk>/', CodexListView.as_view()),

    # ----- My Page -----
    # main
    # path('mypage/<str:userid>/', MyPageView.as_view()),
    # 질문 데이터 조회
    # path('mypage/<int:year>/', ???)
    # path('mypage/<int:year>/<int:month>/', ???)
    # path('mypage/<int:year>/<int:month>/<int:day>/', ???)
]
