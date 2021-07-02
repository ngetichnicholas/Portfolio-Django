from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.home, name='homePage'),
  url(r'projects/', views.projects, name='all_projects'),
  url(r'^search/',views.s)
]