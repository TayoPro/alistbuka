from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    type = Type.objects.all()

    context = {
        'jibola':type
    }
    return render(request, 'index.html',context)
    # return HttpResponse('App installed')

def food(request,id):
    prep = Preparation.objects.filter(type_id=id)   

    context = {
        'barth':prep
    }

    return render(request, 'food.html', context)

