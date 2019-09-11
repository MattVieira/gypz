from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from django.views.generic import TemplateView



class TemplateIndex(LoginRequiredMixin,TemplateView):
    template_name = 'core/index.html'


