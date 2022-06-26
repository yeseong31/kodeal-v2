import jwt
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from common.forms import UserForm
from config.settings.my_settings import EMAIL, JWT_SECRET_KEY


def signup(request):
    """
    회원가입
    """
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            userid = form.cleaned_data.get('username')
            try:
                # 이메일 유효성 검증
                validate_email(email)

                # 이미 존재하는 이메일이라면
                if User.objects.filter(email=email).exists():
                    return JsonResponse({"message": "EXISTS_EMAIL"}, status=400)

                # '활성' 상태를 False로 한 상태로 저장
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                # 이메일 인증 링크 및 데이터 구성
                current_site = get_current_site(request)
                # 도메인
                domain = current_site.domain
                # 입력한 사용자 ID에 대한 암호화
                uidb64 = urlsafe_base64_encode(force_bytes(userid))
                token = jwt.encode({'userid': userid}, JWT_SECRET_KEY, algorithm='HS256').decode('UTF-8')
                message_data = message(domain, uidb64, token)

                # 이메일 메시지 구성
                mail_title = "Kodeal: 이메일 인증을 완료해 주세요."
                EmailMessage(mail_title, message_data, to=[email]).send()

                return redirect('kodeal:index')
            except KeyError:
                return JsonResponse({"message": "INVALID_KEY"}, status=400)
            except TypeError:
                return JsonResponse({"message": "INVALID_TYPE"}, status=400)
            except ValidationError:
                return JsonResponse({"message": "VALIDATION_ERROR"}, status=400)
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def activate(request, uidb64, token):
    """
    이메일 인증 및 사용자 활성화
    """
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        try:
            user = User.objects.get(username=force_str(urlsafe_base64_decode(uidb64)))
            token = jwt.decode(token, JWT_SECRET_KEY, algorithm='HS256')

            # 전달된 두 값이 일치한다면 사용자의 '활성' 상태를 1로 set
            if user.username == token['userid']:
                user.is_active = True
                user.save()
                return redirect(EMAIL['REDIRECT_PAGE'])
            return JsonResponse({"message": "AUTH FAIL"}, status=400)

        except ValidationError:
            return JsonResponse({"message": "TYPE_ERROR"}, status=400)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"}, status=400)


def message(domain, uidb64, token):
    """
    Active를 담당하는 Endpoint URL 주소를 메시지로 Send
    """
    return f"아래 링크를 클릭하면 회원가입 인증이 완료됩니다.\n\n" \
           f"회원가입 링크 : http://{domain}/common/activate/{uidb64}/{token}\n\n" \
           f"감사합니다."
