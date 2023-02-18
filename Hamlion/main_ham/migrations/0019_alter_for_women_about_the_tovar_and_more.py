# Generated by Django 4.0.6 on 2022-12-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_ham', '0018_for_women_color_for_women_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_women',
            name='about_the_tovar',
            field=models.CharField(max_length=3000, null=True, verbose_name='О товаре '),
        ),
        migrations.AlterField(
            model_name='for_women',
            name='articul_tovar',
            field=models.CharField(max_length=20, null=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='for_women',
            name='country',
            field=models.CharField(max_length=20, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='for_women',
            name='name_tovar',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя товара'),
        ),
        migrations.AlterField(
            model_name='for_women',
            name='season',
            field=models.CharField(choices=[('ЛЕТО', 'ЛЕТО'), ('ЗИМА', 'ЗИМА'), ('ОСЕНЬ', 'ОСЕНЬ'), ('ВЕСНА', 'ВЕСНА')], default='ЛЕТО', max_length=5, null=True, verbose_name='Сезон'),
        ),
        migrations.AlterField(
            model_name='for_women',
            name='sostav_tovar',
            field=models.CharField(max_length=100, null=True, verbose_name='Состав'),
        ),
    ]
