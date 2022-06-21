import uuid as uuid

from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    """
    OpenAI Codex Question Model
    """
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_q',
                               verbose_name='질문 작성자')
    content = models.TextField(verbose_name='질문 내용')
    language = models.CharField(max_length=30, verbose_name='사용 언어')
    voter = models.ManyToManyField(User, related_name='voter_q', verbose_name='추천인')
    create_date = models.DateTimeField(verbose_name='생성일')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        if len(str(self.content)) > 30:
            return self.content[:30] + '...'
        return self.content

    class Meta:
        db_table = 'kodeal_question'


class Answer(models.Model):
    """
    OpenAI Codex Answer Model
    """
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_a',
                               verbose_name='답변 작성자')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='연관된 질문')
    content = models.TextField(verbose_name='답변 결과')
    voter = models.ManyToManyField(User, related_name='voter_a', verbose_name='추천인')
    create_date = models.DateTimeField(verbose_name='생성일')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        if len(str(self.content)) > 30:
            return self.content[:30] + '...'
        return self.content

    class Meta:
        db_table = 'kodeal_answer'


class Keyword(models.Model):
    """
    OpenAI Codex Keyword Model
    """
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=100, verbose_name='키워드')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='연관된 질문')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_k', verbose_name='질문 작성자')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'kodeal_keyword'


class Papago(models.Model):
    """
    Papago Answer Model
    """
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='연관된 질문')
    before_question = models.TextField(verbose_name='번역 전')
    after_question = models.TextField(verbose_name='번역 전')
    create_date = models.DateTimeField(verbose_name='생성일')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        return self.after_question

    class Meta:
        db_table = 'kodeal_papago'


class Profile(models.Model):
    """
    Kodeal Profile(Image) Model
    """
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True, verbose_name='이미지')
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, verbose_name='UUID')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='image_owner', verbose_name='이미지 소유자')

    def __str__(self):
        return self.owner

    class Meta:
        db_table = 'kodeal_profile'


class Comment(models.Model):
    """
    Kodeal Comment Model
    """
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_q',
                               verbose_name='코멘트 작성자')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='연관된 질문')
    content = models.TextField(verbose_name='코멘트 내용')
    voter = models.ManyToManyField(User, related_name='voter_c', verbose_name='추천인')
    create_date = models.DateTimeField(verbose_name='생성일')
    modify_date = models.DateTimeField(null=True, blank=True, verbose_name='수정일')

    def __str__(self):
        if len(str(self.content)) > 30:
            return self.content[:30] + '...'
        return self.content

    class Meta:
        db_table = 'kodeal_comment'

