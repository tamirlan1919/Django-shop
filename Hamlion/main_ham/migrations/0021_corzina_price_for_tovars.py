# Generated by Django 4.1.5 on 2023-02-15 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_ham', '0020_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='corzina',
            name='price_for_tovars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_ham.for_man'),
        ),
    ]
