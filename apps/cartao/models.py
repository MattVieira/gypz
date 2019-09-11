from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CardCreate(models.Model):

    name = models.CharField(max_length=100, verbose_name='name')
    cpf =models.CharField(max_length=15, verbose_name='CPF')
    status =models.BooleanField(default=False)
    email = models.EmailField('Email')
    salary = models.FloatField('Salary')
    limit = models.FloatField('Limits the Card', default=0)
    points = models.IntegerField(default=0)
    data  = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


    def __str__(self):
        return self.name

