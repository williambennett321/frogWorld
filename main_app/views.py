from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Frog
from .forms import DetailsForm
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
  template_name = 'home.html'


class FrogCreate(LoginRequiredMixin, CreateView):
  login_url = '/'
  model = Frog
  fields = fields = ['name', 'color_pat', 'fun_fact', 'lifespan']
  success_url = '/frogs/'
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class FrogUpdate(LoginRequiredMixin, UpdateView):
  model = Frog
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['color_pat', 'fun_fact', 'lifespan']

class FrogDelete(LoginRequiredMixin, DeleteView):
  model = Frog
  success_url = '/frogs/'


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required(login_url='/')
def frogs_index(request):
  frogs = Frog.objects.filter(user=request.user)
  return render(request, 'frogs/index.html', { 'frogs': frogs })

@login_required(login_url='/')
def frogs_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  details_form = DetailsForm()
  return render(request, 'frogs/detail.html', {'frog': frog, 'details_form': details_form})

@login_required(login_url='/')
def add_details(request, frog_id):
  form = DetailsForm(request.POST)
  if form.is_valid():
    new_details = form.save(commit=False)
    new_details.frog_id = frog_id
    new_details.save()
  return redirect('frogs_detail', frog_id=frog_id)
  pass

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('frogs_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)