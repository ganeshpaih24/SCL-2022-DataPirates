from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def login_home(request):
    return render(request, 'user/home.html')

def login_about(request):
    return render(request, 'user/about.html')



#to be added after register view
@login_required
def profile(request):
    return render(request,"user/profile.html")
