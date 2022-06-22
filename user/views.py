from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login_home(request):
    return render(request, 'user/home.html')

def login_about(request):
    return render(request, 'user/about.html')

def register(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}:')
            return redirect('user-login-home')
    else
        form=UserCreationForm()
    return render(request,'user/register.html',{'form':form}})
