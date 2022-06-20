# Generated by Django 4.0.3 on 2022-06-20 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kodeal', '0002_alter_question_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='keyword',
        ),
        migrations.AddField(
            model_name='keyword',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author_k', to=settings.AUTH_USER_MODEL, verbose_name='질문 작성자'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keyword',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kodeal.question', verbose_name='연관된 질문'),
            preserve_default=False,
        ),
    ]
