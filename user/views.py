from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def login_home(request):
    return render(request, 'user/home.html')

def login_about(request):
    return render(request, 'user/about.html')

def register(request):
    form=UserCreationForm()
    return render(request,'user/register.html',{'form':form}})
