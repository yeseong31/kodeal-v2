from django import forms

from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        # 사용할 모델
        model = Question
        # Form에서 사용할 Question 모델의 속성
        fields = ['subject', 'content']
        # Form에 Bootstrap 적용
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }
        # Form Label 편집
        labels = {
            'subject': '제목',
            "content": '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        # 사용할 모델
        model = Answer
        # Form에서 사용할 Question 모델의 속성
        fields = ['content']
        # Form Label 편집
        labels = {
            "content": '답변 내용',
        }
