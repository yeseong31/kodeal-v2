from django.contrib import admin


# 질문 검색
from pybo.models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['sbject']


admin.site.register(Question, QuestionAdmin)
