# Generated by Django 2.2.5 on 2019-09-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartao', '0002_cardcreate_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardcreate',
            name='limit',
            field=models.FloatField(default=0, verbose_name='Limits the Card'),
        ),
    ]
