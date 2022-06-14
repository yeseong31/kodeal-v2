from django import template

register = template.Library()


# 페이지에 표시되는 객체의 순서번호를 역순으로 출력
@register.filter
def sub(value, arg):
    return value - arg
