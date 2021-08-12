from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Project
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def home(requst):
  return render(requst, 'index.html')

def resume(requst):
  return render(requst, 'resume.html')

def services(requst):
  return render(requst, 'services.html')

def contact(requst):
  return render(requst, 'contact.html')

def about(requst):
  return render(requst, 'about.html')

def portfolio(request):
  projects = Project.objects.all().order_by('-published_on')
  return render(request, 'projects.html', {'projects':projects})

def detail(request,portfolio_id):
  try:
    portfolio = get_object_or_404(Project, pk = portfolio_id)
  except ObjectDoesNotExist:
    raise Http404()
  return render(request, 'portfolio.html', {'portfolio':portfolio})

def search_portfolio(request):
  if 'project' in request.GET and request.GET["project"]:
    search_term = request.GET.get("project")
    searched_projects = Project.search_project_title(search_term)
    message = f"{search_term}"

    return render(request,'search.html', {"message":message,"projects":searched_projects})

  else:
    message = "You haven't searched for any term"
    return render(request,'search.html',{"message":message})