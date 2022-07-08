from rest_framework import serializers

from kodeal.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Question 조회 Serializer"""

    class Meta:
        model = Question
        fields = ('id', 'author', 'content', 'language', 'voter', 'create_date', 'modify_date')


class QuestionCreateSerializer(serializers.ModelSerializer):
    """Question 등록 Serializer"""

    class Meta:
        model = Question
        fields = ('content', 'language')
