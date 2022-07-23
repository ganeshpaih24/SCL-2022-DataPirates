from .models import Post
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def login_about(request):
    context={
        'posts':Post.objects.all()
    }  
    return render(request, 'base.html')

@login_required
def profile(request):
    return render(request,"user/profile.html")

    else:
        form=UserRegisterForm()
    return render(request,'user/register.html',{'form':form})
