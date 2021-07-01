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