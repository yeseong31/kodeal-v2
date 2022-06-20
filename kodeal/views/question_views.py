from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from kodeal.forms import QuestionForm
from kodeal.models import Answer, Keyword
from kodeal.views.api.codex import question_to_codex, extract_answer_sentences, get_answer_and_keyword
from kodeal.views.api.papago import papago


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
            # -------------------- 답변 처리 --------------------
            # 한글로 입력된 문장을 Papago API를 이용하여 번역
            translate_question = papago(content)
            # 번역 결과에 대해 OpenAI Codex의 결과 값을 get
            context = get_answer_and_keyword(translate_question, language)
            # DB에 OpenAI Codex로부터 얻은 답변 데이터 저장
            codex_answer = Answer(
                content=context['answer'],
                create_date=timezone.now(),
                author=request.user,
                question=codex_question
            )
            codex_answer.save()
            # -------------------- 키워드 처리 --------------------
            for keyword in context['keywords']:
                Keyword(content=keyword, author=request.user, question=codex_question).save()

            return redirect('kodeal:qna')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'kodeal/qna/question_form.html', context)
