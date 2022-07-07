from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def login_home(request):
    return render(request, 'base.html')

def login_about(request):
    context={
        'posts':Post.objects.all()
    }  
    return render(request, 'base.html')

def login_about(request):
    return render(request, 'user/about.html')


@login_required
def profile(request):
    return render(request,"user/profile.html")

def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}:')
            return redirect('user-login-home')
    else:
        form=UserRegisterForm()
    return render(request,'user/register.html',{'form':form})

class PostListView(ListView):
    model=Post
    template_name='user/home.html'
    context_object_name='posts'
    ordering=['date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
