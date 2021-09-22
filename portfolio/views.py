from portfolio.models import *
from django.shortcuts import render
from django.http import HttpResponse, Http404
import os

# returns the index page of the site


def index(request):
    return render(request, 'index.html', context=None)

# retunrs the education page of the site


def education(request):
    educ_list = Education.objects.all()
    context = {"educ_list": educ_list}
    return render(request, 'education.html', context=context)

# returns the projects page of the site


def projects(request):
    project_list = Projects.objects.all()
    total_projects = len(project_list)
    context = {"project_list": project_list, "n": range(total_projects)}
    return render(request, 'projects.html', context=context)
