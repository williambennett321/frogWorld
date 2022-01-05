from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('frogs/', views.frogs_index, name='frogs_index'),
  path('frogs/<int:frog_id>/', views.frogs_detail, name='frogs_detail'),
]