from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from common.forms import UserForm


def signup(request):
    """
    회원가입
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # form.cleaned_data.get()으로 Form의 입력값을 개별적으로 얻음
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(request, username=username, password=raw_password)

            # Form 저장 시 사용자 저장 및 인증 호출이 자동으로 이루어지므로 위의 과정 생략
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('kodeal:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
