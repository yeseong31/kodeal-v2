from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:signin')
def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user    # author 속성에 로그인 한 사용자의 계정을 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            # return redirect('pybo:detail', question_id=question_id)
            return redirect(f'{resolve_url("pybo:detail", question_id=question_id)}#answer_{answer.id}')
    else:
        return HttpResponseNotAllowed('POST 요청만 가능합니다.')
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:signin')
def answer_modify(request, answer_id):
    """
    pybo 답변 수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '답변 수정 권한이 없습니다.')    # messages: Django 모듈(넌필드 오류 발생 시 사용)
        # return redirect('pybo:detail', question_id=answer.question.id)
        return redirect(f'{resolve_url("pybo:detail", question_id=answer.question.id)}#answer_{answer.id}')
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            # return redirect('pybo:detail', question_id=answer.question.id)
            return redirect(f'{resolve_url("pybo:detail", question_id=answer.question.id)}#answer_{answer.id}')
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:signin')
def answer_delete(request, answer_id):
    """
    pybo 답변 삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '답변 삭제 권한이 없습니다.')  # messages: Django 모듈(넌필드 오류 발생 시 사용)
    else:
        answer.delete()
    # return redirect('pybo:detail', question_id=answer.question.id)
    return redirect(f'{resolve_url("pybo:detail", question_id=answer.question.id)}#answer_{answer.id}')
