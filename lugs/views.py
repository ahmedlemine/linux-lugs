from django.shortcuts import render
from django.http import HttpResponse
from .models import Lug


def home(request):
    context = {
        'lugs': Lug.objects.all()
    }
    return render(request, 'lugs/home.html', context)

def about(request):
    return render(request, 'lugs/about.html', {'title': 'About'})