from dataclasses import fields
from django import forms

from app1.models import Info

class InfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=150)
    email = forms.EmailField()

class InfoModelForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'