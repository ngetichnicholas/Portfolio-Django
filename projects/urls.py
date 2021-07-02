from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.home, name='homePage'),
  url(r'^projects/', views.projects, name='allProjects'),
  url(r'^search/',views.search_projects,name='searchProjects'),
  url(r'^project/(d+)',views.project, name='project')
]

if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)