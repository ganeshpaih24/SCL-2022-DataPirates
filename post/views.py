from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse





class PostListView(ListView):
    model=Post
    template_name='post/home.html'
    context_object_name='posts'
    ordering=['date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def get_template_names(self):
        if self.request.htmx:
            return ["post/htmx_form.html"]
        else:
            return ["post/post_form.html"]
    
    def form_valid(self,form):
        form.instance.author=self.request.user
        super().form_valid(form)

        self.object=form.save(commit=False)
        if self.request.htmx:
            return render(self.request, 'post/htmx_form.html')
        else:
            return reverse('post-detail', kwargs={'pk': self.object.id})

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

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False