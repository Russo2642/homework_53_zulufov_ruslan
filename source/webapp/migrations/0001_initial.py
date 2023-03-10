# Generated by Django 4.1.6 on 2023-02-13 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Опишите задачу', max_length=300, verbose_name='Описание')),
                ('status', models.CharField(default='new', max_length=200, verbose_name='Статус')),
                ('completion_at', models.DateField(blank=True, verbose_name='Дата дедлайна')),
            ],
        ),
    ]
