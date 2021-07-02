from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Project
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(requst):
  return render(requst, 'index.html')

def projects(request):
  projects = Project.get_projects()
  return render(request, 'projects.html', {'projects':projects})

def project(request,id):
  try:
    project = Project.objects.get(id = id).first()
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'project.html', {'project':project})

def search_projects(request):
  if 'project' in request.GET and request.GET["project"]:
    search_term = request.GET.get("project")
    searched_projects = Project.search_project_title(search_term)
    message = f"{search_term}"

    return render(request,'search.html', {"message":message,"projects":searched_projects})

  else:
    message = "You haven't searched for any term"
    return render(request,'search.html',{"message":message})