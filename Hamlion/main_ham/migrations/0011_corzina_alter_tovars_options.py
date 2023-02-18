# Generated by Django 4.0.6 on 2022-12-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_ham', '0010_for_man_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corzina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_clothes', models.IntegerField(null=True, verbose_name='ID товара ')),
                ('accounte', models.CharField(max_length=50, null=True, verbose_name='login')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.AlterModelOptions(
            name='tovars',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
