from django.shortcuts import render
from .models import TestModel

def index(request):
    if request.POST:
        data = request.POST
        success = TestModel.objects.create(
            first_name=data['fname'],
            city=data['dd'],
            email=data['email'],
            car=data['car'],
            song=data['song'],
            mobile=data['mobile'],
        )
        if success:
            print("Ma'lumotlar muvaffaqiyatli saqlandi!!!")
    query = TestModel.objects.all()
    context = {
        'query': query,
    }        
    return render(request, 'index.html', context=context)