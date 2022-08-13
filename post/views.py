from multiprocessing import context
from .models import Post, SubPost, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .forms import SubPostModelForm, PostCommentForm, PostForm
from django.shortcuts import get_object_or_404
#from django.http import HttpResponseRedirect
from email.policy import HTTP
import http
from http.client import HTTPResponse
from django.shortcuts import HttpResponse
from .models import Post,SubPost,Comment


class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            post=self.get_object()).order_by('-created')
        if self.request.user.is_authenticated:
            context['comment_form'] = PostCommentForm(
                instance=self.request.user)
        return context
    '''
    def get_queryset(self, *args, **kwargs):
        return SubPost.objects.filter(post_id=self.kwargs['pk'])
    '''

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get(
            'body'), user=self.request.user, post=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


'''
class CommentCreateView(CreateView):
    model = Comment
    form_class = PostCommentForm
    template_name='post/add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url="/post/{post_id}"
'''


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'New Post Created! Enter details..')
        return super().form_valid(form)


'''
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
'''


@login_required
def postUpdateView(request, pk):
    context = {}
    obj = get_object_or_404(Post, id=pk)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Post Updated!')
        return redirect('post-detail', pk=pk)
    context["form"] = form
    return render(request, "post/post_update.html", context)



@login_required
def deletePost(request, pk):
    post = Post.objects.get(id=pk).delete()
    messages.success(request, f'Your Post information has been deleted')
    return redirect('user-home')




@login_required
def deletePost(request,pk):
    post = Post.objects.get(id=pk).delete()
    messages.success(request, f'Your Post information has been deleted')
    return redirect('user-home')

def flowchart(request):
    subpost = SubPost.objects.all()
    context = {'subpost': subpost}
    return render(request, 'post/flow2.html',context)
    
@login_required
def deleteSubpost(request, pk, id):
    subpost = SubPost.objects.get(id=id).delete()
    messages.success(request, f'Your subpost information has been deleted')
    return redirect('post-detail', pk=pk)




@login_required
def createSubpost(request, pk):
    post = Post.objects.get(id=pk)
    form = SubPostModelForm()
    if request.method == 'POST':
        form = SubPostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-subpost')
    context = {'form': form}
    return render(request, 'post/subpost_form.html', context)
    


class SubPostCreateView(CreateView):
    model = SubPost
    form_class = SubPostModelForm
    template_name = 'post/subpost_form.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = "/post/{post_id}"


@login_required
def updateSubpost(request, pk, id):
    subpost = SubPost.objects.get(id=id)
    context = {}
    form = SubPostModelForm(request.POST or None, instance=subpost)
    if form.is_valid():
        form.save()
        messages.success(request, f'Subpost updated!')
        return redirect('post-detail', pk=pk)
    context["form"] = form
    return render(request, "post/subpost-update.html", context)

@login_required
def star(request,pk):
    user=request.user
    post=get_object_or_404(Post,id=pk)
    current_stars=post.stars_count
    s,created=Star.objects.get_or_create(user=user)
    if s.posts.filter(id=pk).exists():
        s.posts.remove(post)
        current_stars=current_stars-1
        messages.success(request, f'Post removed from Starred Posts List!')
    else:
        s.posts.add(post)
        current_stars=current_stars+1
        messages.success(request, f'Post added to Starred Posts List!')
    post.stars_count=current_stars
    post.save()
    return redirect('post-detail',pk=pk)

@login_required
def starred_list(request):
    stars=Post.author.filter(stars=request.user)
    return render(request,"post/stars.html",{'stars':stars})
    

def search(request):
    query=request.GET['query']
    #allposts=Post.objects.all()
    allposts=Post.objects.filter(title__icontains=query)
    print(allposts[0])
    params={'allpost':allposts}
    return render(request, 'post/search.html', params)
    #return HttpResponse('This is search')