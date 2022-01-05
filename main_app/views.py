from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
  return HttpResponse('<h1>Welcome</h1>')

def about(request):
  return render(request, 'about.html')

def frogs_index(request):
  return render(request, 'frogs/index.html', { 'frogs': frogs })