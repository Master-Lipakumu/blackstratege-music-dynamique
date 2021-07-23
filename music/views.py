from django.shortcuts import render, redirect

import random

from .models import Video

from .form import Contacte

# Create your views here.


def contacte(request):
    #form = Contacte.objects.all()
    if request.method == "POST":
        form = Contacte(request.POST).save()

        return redirect('index')
    else:
        form = Contacte()
    return render(request,'music/contacte.html', {'form':form})


def index(request):
    full_list = Video.objects.all()

    full_list = list(full_list)

    full_list = full_list[::-1]

    context={'full_list':full_list}

    return render(request,'index.html', context)
