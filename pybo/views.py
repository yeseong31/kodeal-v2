from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question, Answer


def index(request):
    """
    전체 질문 목록 조회
    """
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    page = request.GET.get('page', '1')    # '/pybo/?page=1' 형태로 호출된 URL에서 page를 가져옴
    paginator = Paginator(question_list, 10)    # 한 페이지 당 10개의 질문
    page_obj = paginator.get_page(page)    # 페이징 객체 생성

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    해당 id를 가지는 질문 조회
    """
    # 해당 데이터가 존재하지 않는 경우 404 페이지 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


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
            return redirect('pybo:detail', question_id=question_id)
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
        return redirect('pybo:detail', question_id=answer.question.id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
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
    return redirect('pybo:detail', question_id=answer.question.id)
