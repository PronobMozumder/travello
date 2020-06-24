from django.shortcuts import render
from . models import destination,info


def index(request):
    dests = destination.objects.all()
    return render(request, 'index.html', {'dests': dests})


def about(request):
    return render(request, 'about.html', {})


def test(request):
    print("hi")
    return render(request, 'test.html',)
