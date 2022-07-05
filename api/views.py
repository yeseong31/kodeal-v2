import traceback

from django.contrib.auth.models import User
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import RegisterSerializer, SigninSerializer
from common.tokens import account_activation_token


class CheckIDView(APIView):
    """아이디 중복 확인"""

    def post(self, request):
        if User.objects.filter(username=request.data['username']):
            return Response({'message': '이미 존재하는 사용자입니다.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': '사용 가능한 아이디입니다.'}, status=status.HTTP_200_OK)


class CheckEmailView(generics.GenericAPIView):
    """이메일 인증"""
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': '이메일 인증 링크를 발송하였습니다. 이메일을 확인해 주세요.'},
                status=status.HTTP_200_OK)
        return Response(
            {'message': '해당 아이디와 이메일로 인증을 수행할 수 없습니다.'},
            status=status.HTTP_400_BAD_REQUEST)


class UserActivateView(APIView):
    """이메일 인증 및 사용자 활성화"""

    def get(self, request, uidb64, token):
        # 사용자 확인
        try:
            user = get_object_or_404(User, pk=force_str(urlsafe_base64_decode(uidb64)))
        except(TypeError, ValueError, OverflowError):
            user = None
        # Token 유효성 검증
        try:
            if user is not None:
                if account_activation_token.check_token(user, token):
                    user.is_active = True
                    user.save()
                    return Response({'message': '인증되었습니다.'}, status=status.HTTP_200_OK)
                else:
                    # 인증이 만료되었다면 해당 계정 삭제
                    user.delete()
                    return Response({'message': '인증이 만료된 링크입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': '잘못된 접근입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(traceback.format_exc())


class SignupView(APIView):
    """회원가입"""

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        password2 = request.data['password2']
        email = request.data['email']

        user = get_object_or_404(User, username=username)
        if not user.is_active:
            return Response({'message': '이메일 인증 링크를 통해 인증을 완료해 주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        if password != password2:
            return Response({'message': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        if user.email != email:
            return Response({'message': '인증을 완료한 이메일과 다른 이메일입니다.'}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(password)
        user.save()
        Token.objects.create(user=user)  # 해당 계정에 대한 Token 발행
        return Response({'message': '회원가입이 완료되었습니다.'}, status=status.HTTP_200_OK)


class SigninView(generics.GenericAPIView):
    """로그인"""
    serializer_class = SigninSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data  # validate()의 return 값
        return Response({'token': token.key}, status=status.HTTP_200_OK)
