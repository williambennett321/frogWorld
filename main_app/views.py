from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Frog
from .forms import DetailsForm
from django.http import HttpResponse

class FrogCreate(CreateView):
  model = Frog
  fields = fields = ['name', 'color_pat', 'fun_fact', 'lifespan']
  success_url = '/frogs/'

class FrogUpdate(UpdateView):
  model = Frog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['color_pat', 'fun_fact', 'lifespan']

class FrogDelete(DeleteView):
  model = Frog
  success_url = '/frogs/'


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
  details_form = DetailsForm()
  return render(request, 'frogs/detail.html', {'frog': frog, 'details_form': details_form})

def add_details(request, frog_id):
  form = DetailsForm(request.POST)
  if form.is_valid():
    new_details = form.save(commit=False)
    new_details.frog_id = frog_id
    new_details.save()
  return redirect('frogs_detail', frog_id=frog_id)
  pass