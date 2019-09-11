from django.contrib import admin
from django.urls import path, include
from apps.cartao.api.urls import router_card
from rest_framework.authtoken.views import obtain_auth_token

from apps.core.views import TemplateIndex

urlpatterns = [
    path('', TemplateIndex.as_view(), name="home"),

]