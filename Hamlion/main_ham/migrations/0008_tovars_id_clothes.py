# Generated by Django 4.0.6 on 2022-12-06 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_ham', '0007_alter_tovars_accounte'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovars',
            name='id_clothes',
            field=models.IntegerField(null=True, verbose_name='ID товара '),
        ),
    ]