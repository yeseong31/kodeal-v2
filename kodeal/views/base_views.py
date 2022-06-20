import math

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from kodeal.models import Question


def index(request):
    """
    Kodeal Main Page
    """
    return render(request, 'kodeal/home.html')


@login_required(login_url='common:signin')
def qna(request):
    """
    Kodeal QnA Page
    """
    question_list = Question.objects.order_by('-create_date')

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
    return render(request, 'kodeal/qna/index.html', context)
