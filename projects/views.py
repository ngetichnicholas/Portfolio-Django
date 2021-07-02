from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Project

# Create your views here.
def home(requst):
  return render(requst, 'index.html')

def projects(request):
  projects = Project.get_projects()
  return render(request, 'projects.html', {'projects':projects})

def project(request,project_id):
  try:
    project = Project.objects.get(id = project_id)
  except DoesNotExist:
    raise Http404()
  return render(request, 'project.html', {'project':project})