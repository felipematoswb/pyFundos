from dataclasses import fields
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={
                    "placeholder": "Name task...",
                    "class": "form-control",
                }
            ))
    description = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={
                    "placeholder": "Describe task...",
                    "class": "form-control",
                }
            ))
    class Meta:
        model = Todo
        fields = '__all__'