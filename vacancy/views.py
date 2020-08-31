from django.shortcuts import render
from django.views.generic import ListView
from . models import Vacancy
# Create your views here.

class VacanciesView(ListView):
    model = Vacancy
    template_name = 'vacancies.html'