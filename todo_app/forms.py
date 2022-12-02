from dataclasses import fields
from pyexpat import model
from . models import Task
from django import forms

class todoforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']