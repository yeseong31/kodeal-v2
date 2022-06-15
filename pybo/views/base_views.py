from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


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
