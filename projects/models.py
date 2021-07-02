from django.db import models
import datetime as dt

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=30)
  sur_name = models.CharField(max_length=30)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10,blank=True)

  def __str__(self):
      return self.first_name

  class meta:
    ordering =['name']

  def save_author(self):
    self.save()

class Project(models.Model):
  title = models.CharField(max_length=60)
  description  = models.TextField()
  author = models.ForeignKey(Author)
  published_on = models.DateTimeField(auto_now_add=True)
  project_image = models.ImageField(upload_to = 'projects/')

  def __str__(self):
      return self.title

  @classmethod
  def get_projects():
    all_projects = Project.objects.all().order_by(Project.published_on.desc())
    return all_projects

  @classmethod
  def search_project_title(cls,search_term):
    search_projects = cls.objects.filter(title__icontains=search_term)
    return search_projects