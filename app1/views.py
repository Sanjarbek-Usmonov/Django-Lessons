import email
from django.shortcuts import render
from .models import *
from .forms import InfoForm, InfoModelForm

def index(request):
    form = InfoModelForm()
    if request.method == 'POST':
        form = InfoModelForm(request.POST)
        if form.is_valid():
            # ins = Info(
            #     name = form.cleaned_data['name'],
            #     mobile = form.cleaned_data['mobile'],
            #     email = form.cleaned_data['email'],
            # )
            # ins.save()
            form.save()
            return render(request, 'index.html')
        
    else: 
        form = InfoModelForm()
    return render(request, 'index.html', {'form': form})

