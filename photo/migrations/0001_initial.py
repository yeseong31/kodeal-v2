# Generated by Django 4.0.3 on 2022-06-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'photo',
            },
        ),
    ]
