from django import forms
from .models import *

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = '__all__'
