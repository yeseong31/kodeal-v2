from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import resolve_url, redirect, render, get_object_or_404
from django.utils import timezone

from kodeal.forms import CommentForm
from kodeal.models import Question, Comment


@login_required(login_url='common:signin')
def comment_create(request, question_id):
    """
    Kodeal 코멘트 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user    # author 속성에 로그인 한 사용자의 계정을 저장
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect(f'{resolve_url("kodeal:question_detail", question_id=question_id)}#comment_{comment.id}')
    else:
        return HttpResponseNotAllowed('Allow POST requests only.')
    context = {'question': question, 'form': form}
    return render(request, 'kodeal/qna/question_detail.html', context)


@login_required(login_url='common:signin')
def comment_vote(request, comment_id):
    """
    Kodeal 코멘트 추천
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user == comment.author:
        messages.error(request, '본인이 작성한 글은 추천할 수 없습니다.')
    else:
        comment.voter.add(request.user)
    return redirect(f'{resolve_url("kodeal:question_detail", question_id=comment.question.id)}#comment_{comment.id}')


@login_required(login_url='common:signin')
def comment_modify(request, comment_id):
    """
    Kodeal 코멘트 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '코멘트 수정 권한이 없습니다.')
        return redirect(f'{resolve_url("kodeal:question_detail", question_id=comment.question.id)}#comment_{comment.id}')
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect(f'{resolve_url("kodeal:question_detail", question_id=comment.question.id)}#comment_{comment.id}')
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'kodeal/qna/comment_form.html', context)


@login_required(login_url='common:signin')
def comment_delete(request, comment_id):
    """
    Kodeal 코멘트 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    # 관리자 및 작성자인 경우
    if request.user.is_staff or request.user == comment.author:
        comment.delete()
    # 작성자가 아닌 경우
    else:
        messages.error(request, '답변 삭제 권한이 없습니다.')  # messages: Django 모듈(넌필드 오류 발생 시 사용)
    return redirect(f'{resolve_url("kodeal:question_detail", question_id=comment.question.id)}#comment_{comment.id}')
