# Generated by Django 4.0.6 on 2022-12-14 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_ham', '0014_alter_corzina_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeTovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_clothes', models.IntegerField(null=True, verbose_name='ID товара ')),
                ('accounte', models.CharField(max_length=50, null=True, verbose_name='login')),
                ('like', models.BooleanField(verbose_name='Выбран')),
            ],
            options={
                'verbose_name': 'Лайкнутый товар',
                'verbose_name_plural': 'Лайкнутый товары',
            },
        ),
    ]