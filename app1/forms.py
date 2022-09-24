from dataclasses import fields
from django import forms
from app1.models import Info


class InfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=150)
    email = forms.CharField()

    def clean_mobile(self):
        number = self.cleaned_data['mobile']
        qs = Info.objects.filter(mobile=number)
        if qs:
            raise forms.ValidationError('Bu mobil raqam oldin kiritilgan!')
        return number

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = Info.objects.filter(email=email)
        if qs:
            raise forms.ValidationError('Bu email oldin kiritilgan!')
        elif '@' not in email or '.' not in email:
            raise forms.ValidationError('Email noto\'g\'ri kiritildi!')
        return email

class InfoModelForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'