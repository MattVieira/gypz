from django.contrib import admin

# Register your models here.
from apps.cartao.models import CardCreate


class CardCreateAdmin(admin.ModelAdmin):
    list_display = ['id','name','cpf','status']


admin.site.register(CardCreate,CardCreateAdmin)