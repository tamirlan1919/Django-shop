# Generated by Django 4.0.6 on 2022-12-14 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_ham', '0015_liketovar'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikeTovar',
        ),
        migrations.AddField(
            model_name='tovars',
            name='like',
            field=models.BooleanField(null=True, verbose_name='Выбран'),
        ),
    ]