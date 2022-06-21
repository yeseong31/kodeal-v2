from django.contrib import admin

# 질문 검색
from django.contrib.auth.models import Group

from kodeal.models import Question, Answer, Comment, Keyword


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['content', 'language']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)

admin.site.unregister(Group)
