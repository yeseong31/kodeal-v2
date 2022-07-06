from django import forms

from kodeal.models import Question, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        # 사용할 모델
        model = Question
        # Form에서 사용할 Question 모델의 속성
        fields = ['content', 'language']
        # Form에 Bootstrap 적용
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'language': forms.TextInput(attrs={'class': 'form-control'})
        }
        # Form Label 편집
        labels = {
            "content": '질문',
            'language': '언어',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        # 사용할 모델
        model = Comment
        # Form에서 사용할 Question 모델의 속성
        fields = ['content']
        # Form Label 편집
        labels = {
            "content": '코멘트 내용',
        }

