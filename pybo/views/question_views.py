from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:signin')
def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # form의 유효성 검사
        if form.is_valid():
            # 임시 저장하여 question 객체를 return 받음
            question = form.save(commit=False)
            # author 속성에 로그인 한 사용자의 계정을 저장
            question.author = request.user
            # create_date 속성은 데이터 저장 시점에 생성해야 하는 값이므로 QuestionForm에 등록하여 사용하지 않음
            from django.utils import timezone
            question.create_date = timezone.now()
            # 데이터를 실제로 저장
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:signin')
def question_modify(request, question_id):
    """
    pybo 질문 수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        from django.contrib import messages
        messages.error(request, '질문 수정 권한이 없습니다.')    # messages: Django 모듈(넌필드 오류 발생 시 사용)
        return redirect('pybo:detail', question_id=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:signin')
def question_delete(request, question_id):
    """
    pybo 질문 삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '질문 삭제 권한이 없습니다.')    # messages: Django 모듈(넌필드 오류 발생 시 사용)
        return redirect('pybo:detail', question_id=question_id)
    else:
        question.delete()
    return redirect('pybo:index')


@login_required(login_url='common:signin')
def question_vote(request, question_id):
    """
    pybo 질문 추천
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)    # 동일한 사용자에 의해 계속 호출되더라도 ManyToManyField에서 자체 처리함
    return redirect('pybo:detail', question_id=question.id)
