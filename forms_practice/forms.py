from django import forms
from django.forms import fields
from .models import FormsModel


class MyForm(forms.Form):
    name = forms.CharField(max_length=20)

    def clean_name(self):
        name = self.cleaned_data['name']
        print("I am from ", self.cleaned_data)
        return name.lower()


class FormsModelForm(forms.ModelForm):
    class Meta:
        model = FormsModel
        fields = ['name', 'email']
