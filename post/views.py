from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'post/base.html')


def about(request):
    return render(request, 'post/about.html')

