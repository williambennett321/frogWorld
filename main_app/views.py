from django.shortcuts import render
from .models import Frog
from django.http import HttpResponse


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def frogs_index(request):
  frogs = Frog.objects.all()
  return render(request, 'frogs/index.html', { 'frogs': frogs })

def frogs_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  return render(request, 'frogs/detail.html', {'frog': frog})