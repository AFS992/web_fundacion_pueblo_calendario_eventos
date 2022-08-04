from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class Calendario(TemplateView):
    template_name='calendario-dinamico.html'
