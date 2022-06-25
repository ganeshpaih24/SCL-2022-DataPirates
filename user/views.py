from django.shortcuts import render



def login_home(request):
    return render(request, 'base.html')

def login_about(request):
    return render(request, 'base.html')
