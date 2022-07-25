from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from kodeal.models import Answer


@login_required(login_url='common:signin')
def answer_vote(request, question_id):
    """
    Kodeal 답변 추천
    """
    answer = get_object_or_404(Answer, question=question_id)
    if request.user in answer.voter.all():
        answer.voter.remove(request.user)
    else:
        answer.voter.add(request.user)
    return redirect('kodeal:question_detail', question_id=question_id)
