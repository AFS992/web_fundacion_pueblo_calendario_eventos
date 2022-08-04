from django.shortcuts import render
from django.views.generic import TemplateView

class Inicio(TemplateView):
    template_name='index.html'

class login(TemplateView):
    template_name='login.html'