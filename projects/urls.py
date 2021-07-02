from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.home, name='homePage'),
  path('projects/', views.projects, name='allProjects'),
  path('search/',views.search_projects,name='searchProjects'),
  path('project/<int:project_id>/',views.project, name='project')
]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)