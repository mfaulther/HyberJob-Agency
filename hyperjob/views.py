from django.views.generic import TemplateView
from django.shortcuts import render

class MenuView(TemplateView):
    template_name = 'menu.html'