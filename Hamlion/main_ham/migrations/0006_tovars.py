# Generated by Django 4.0.6 on 2022-12-06 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_ham', '0005_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tovars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounte', models.CharField(max_length=50, verbose_name='login')),
            ],
            options={
                'verbose_name': 'Аккаунты',
                'verbose_name_plural': 'Аккаунт',
            },
        ),
    ]
