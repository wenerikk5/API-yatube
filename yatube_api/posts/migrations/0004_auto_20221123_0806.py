# Generated by Django 2.2.16 on 2022-11-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20221122_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Введите комментарий', verbose_name='Комментарий'),
        ),
    ]