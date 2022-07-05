from rest_framework.views import APIView


class CodexListView(APIView):
    """OpenAI Codex API"""

    def get(self, pk: int):
        """특정 사용자의 질문 목록 조회"""
        pass

    def post(self):
        """OpenAI Codex 질문&답변 생성"""
        pass
