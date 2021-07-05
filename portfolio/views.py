from portfolio.models import *
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html', context=None)


def education(request):
    educ_list = Education.objects.all()
    context = {"educ_list": educ_list}
    return render(request, 'education.html', context=context)


def projects(request):
    project_list = Projects.objects.all()
    total_projects = len(project_list)
    context = {"project_list": project_list, "n": range(total_projects)}
    return render(request, 'projects.html', context=context)
