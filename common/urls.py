from django.urls import path
from django.contrib.auth import views as auth_views

from common import views

app_name = 'common'

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='common/signin.html'), name='signin'),    # 로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    # 로그아웃
    path('signup/', views.signup, name='signup'),    # 회원가입
]
