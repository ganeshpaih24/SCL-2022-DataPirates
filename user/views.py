from django.shortcuts import render
from .models import Post




def login_home(request):
    data=Post.objects.all()
    context={
        'posts':Post.objects.all()
    }  
    for i in data:
        print(i)
    
    return render(request, 'user/home.html')

def login_about(request):
    return render(request, 'user/about.html')
