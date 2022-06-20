from django.urls import path
from django.contrib.auth import views as auth_views

from common.views import activate, signup

app_name = 'common'

urlpatterns = [
    # 로그인
    path('signin/', auth_views.LoginView.as_view(template_name='common/signin.html'), name='signin'),
    # 로그아웃
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # 회원가입
    path('signup/', signup, name='signup'),
    # 이메일 인증
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
]
