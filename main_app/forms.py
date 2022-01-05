from django.forms import ModelForm
from .models import Details

class DetailsForm(ModelForm):
  class Meta:
    model = Details
    fields = ['species', 'diet', 'habitat']