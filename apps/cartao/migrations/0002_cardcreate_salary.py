# Generated by Django 2.2.5 on 2019-09-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardcreate',
            name='salary',
            field=models.FloatField(default=1, verbose_name='Salary'),
            preserve_default=False,
        ),
    ]
