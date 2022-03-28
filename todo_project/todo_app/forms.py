from django import forms
from .models import TodoData


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoData
        fields = ['name', 'priority','date',]
