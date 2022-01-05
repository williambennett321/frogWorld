from django.db import models

# Create your models here.
class Frog(models.Model):
  name = models.CharField(max_length=100)
  color_pat = models.CharField(max_length=100)
  fun_fact = models.TextField(max_length=250)
  lifespan = models.IntegerField()

  def __str__(self):
    return self.name