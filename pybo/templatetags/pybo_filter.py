import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


# 페이지에 표시되는 객체의 순서번호를 역순으로 출력
@register.filter
def sub(value, arg):
    return value - arg


# 마크다운 적용
@register.filter()
def md(value):
    extensions = ['nl2br', 'fenced_code']
    return mark_safe(markdown.markdown(value, extensions=extensions))
