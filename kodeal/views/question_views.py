import math

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone

from kodeal.forms import QuestionForm
from kodeal.models import Answer, Keyword, Question, Papago
from kodeal.codex import get_answer_and_keyword
from kodeal.papago import papago


@login_required(login_url='common:signin')
def qna(request):
    """
    Kodeal QnA Page
    """
    question_list = Question.objects.order_by('-create_date')

    # 검색 처리
    kw = request.GET.get('kw', '')
    if kw:
        question_list = question_list.filter(
            Q(content__icontains=kw) |  # 질문 내용
            Q(answer__content__icontains=kw) |  # 답변 내용
            Q(author__username__icontains=kw) |  # 질문 등록자
            Q(language__icontains=kw)  # 사용 언어
        ).distinct()  # 중복 제거

    # 페이징 처리
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)  # 한 페이지 당 10개의 질문
    page_obj = paginator.get_page(page)  # 페이징 객체 생성
    # 시작 번호
    temp_end = int(math.ceil(page_obj.number / 10.0)) * 10
    start = temp_end - 9
    # 끝 번호
    total_page = math.ceil(len(question_list) / 10)
    end = temp_end if total_page > temp_end else total_page

    context = {'question_list': page_obj, 'start': start, 'end': end, 'total_page': total_page, 'page': page}
    return render(request, 'kodeal/qna/question_list.html', context)


@login_required(login_url='common:signin')
def question_detail(request, question_id):
    """
    해당 id를 가지는 질문 조회
    """
    # 해당 데이터가 존재하지 않는 경우 404 페이지 출력
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'kodeal/qna/question_detail.html', context)


@login_required(login_url='common:signin')
def question_create(request):
    """
    Kodeal 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            language = form.cleaned_data.get('language')

            # -------------------- 질문 처리 --------------------
            # DB에 OpenAI Codex에 넘길 질문 데이터 저장
            codex_question = form.save(commit=False)
            codex_question.author = request.user
            codex_question.create_date = timezone.now()
            codex_question.save()
            # -------------------- Papago 처리 --------------------
            # 한글로 입력된 문장을 Papago API를 이용하여 번역
            translate_question = papago(content)
            Papago(before_question=content,
                   after_question=translate_question,
                   question=codex_question,
                   create_date=timezone.now()).save()
            # -------------------- 답변 처리 --------------------
            # 번역 결과에 대해 OpenAI Codex의 결과 값을 get
            context = get_answer_and_keyword(translate_question, language)
            # DB에 OpenAI Codex로부터 얻은 답변 데이터 저장
            codex_answer = Answer(
                content=context['answer'],
                author=request.user,
                create_date=timezone.now(),
                question=codex_question)
            codex_answer.save()
            # -------------------- 키워드 처리 --------------------
            for keyword in context['keywords']:
                Keyword(content=keyword, author=request.user, question=codex_question).save()

            alert_message = '질문 등록 완료! 목록을 확인해 주세요.'
            return render(request, 'complete.html', {'message': alert_message,
                                                     'url': f'/question/detail/{codex_question.pk}/'})
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'kodeal/qna/question_form.html', context)


@login_required(login_url='common:signin')
def question_vote(request, question_id):
    """
    Kodeal 질문 추천
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('kodeal:question_detail', question_id=question.id)


@login_required(login_url='common:signin')
def question_delete(request, question_id):
    """
    Kodeal 질문 삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user.is_staff or request.user == question.author:
        question.delete()
        return redirect('kodeal:qna')
    else:
        messages.error(request, '질문 삭제 권한이 없습니다.')    # messages: Django 모듈(넌필드 오류 발생 시 사용)
        return redirect('kodeal:question_detail', question_id=question_id)

