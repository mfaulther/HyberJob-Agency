from django.shortcuts import render
from django.views.generic import ListView
from . models import Resume

# Create your views here.

class ResumeView(ListView):
    model = Resume
    template_name = 'resume.html'
