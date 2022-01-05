from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('frogs/', views.frogs_index, name='frogs_index'),
  path('frogs/<int:frog_id>/', views.frogs_detail, name='frogs_detail'),
  path('frogs/create/', views.FrogCreate.as_view(), name='frogs_create'),
  path('frogs/<int:pk>/update/', views.FrogUpdate.as_view(), name='frogs_update'),
  path('frogs/<int:pk>/delete/', views.FrogDelete.as_view(), name='frogs_delete'),
  path('accounts/signup/', views.signup, name='signup'),
  path('frogs/<int:frog_id>/add_details/', views.add_details, name='add_details'),
]
