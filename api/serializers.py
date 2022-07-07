from rest_framework import serializers

from common.serializers import UserInfoSerializer
from kodeal.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Question 조회 Serializer"""
    user = UserInfoSerializer(read_only=True)  # nested serializer

    class Meta:
        model = Question
        fields = ('id', 'author', 'content', 'language', 'voter', 'create_date', 'modify_date')


class QuestionCreateSerializer(serializers.ModelSerializer):
    """Question 등록 Serializer"""

    class Meta:
        model = Question
        fields = ('content', 'language')
