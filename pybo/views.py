from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from pybo.models import Question


def index(request):
    """
    전체 질문 목록 조회
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    해당 id를 가지는 질문 조회
    """
    # 해당 데이터가 존재하지 않는 경우 404 페이지 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


# 해당 질문에 답변 생성
def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)

    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 위와 동일한 코드
    # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # answer.save()

    return redirect('pybo:detail', question_id=question_id)
