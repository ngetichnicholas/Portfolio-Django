from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Project

# Create your views here.
def home(requst):
  return render(requst, 'index.html')

def projects(request):
  projects = Project.get_projects()