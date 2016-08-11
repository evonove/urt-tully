from django.shortcuts import render
from .models import Data

def datas_list(request):
    datas = Data.objects.all()
    return render(request, 'polls/datas_list.html', {'datas':datas})
