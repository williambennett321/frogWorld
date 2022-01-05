from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Frog(models.Model):
  name = models.CharField(max_length=100)
  color_pat = models.CharField(max_length=100)
  fun_fact = models.TextField(max_length=250)
  lifespan = models.IntegerField()

  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Details(models.Model):
  species = models.CharField(max_length=100)
  diet = models.CharField(max_length=100)
  habitat = models.TextField(max_length=250)

  frog = models.ForeignKey(Frog, on_delete=models.CASCADE)

  def __str__(self):
    return self.species

  def get_absolute_url(self):
    return reverse('frogs_detail', kwargs={'frog_id': self.id})