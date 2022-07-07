from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.permissions import CustomReadOnly
from api.serializers import QuestionSerializer, QuestionCreateSerializer
from kodeal.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [CustomReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return QuestionSerializer
        return QuestionCreateSerializer

    def perform_create(self, serializer):
        question = Question.objects.get(user=self.request.user)
        serializer.save(author=self.request.user)
