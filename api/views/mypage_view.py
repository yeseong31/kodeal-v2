from rest_framework.views import APIView


class MyPageView(APIView):
    """마이페이지"""

    def get(self):
        """특정 사용자의 마이페이지 정보 조회"""
        pass
