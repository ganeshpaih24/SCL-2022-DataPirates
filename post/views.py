from .models import Post,SubPost,Comment
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
from django.urls import reverse,reverse_lazy
from .forms import SubPostModelForm,PostCommentForm





class PostListView(ListView):
    model=Post
    template_name='post/home.html'
    context_object_name='posts'
    ordering=['date_posted']

class PostDetailView(DetailView):
    model=Post
    template_name = 'post/post_detail.html'
    '''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['comment'] = PostComment.objects.all()
        context['form'] = PostCommentForm()
        return context
      
    def get_queryset(self, *args, **kwargs):
        return SubPost.objects.filter(post_id=self.kwargs['pk'])
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

def flowchart(request):
    subpost = SubPost.objects.all()
    context = {'subpost': subpost}
    return render(request, 'post/flow2.html',context)
    
'''    
@login_required
def subpost(request,pk):
    subposts = SubPost.objects.filter(pk=pk)
    context = {'subposts': subposts}
    return render(request,'post/post_detail.html',context)
'''

@login_required
def createSubpost(request,pk):
    post=Post.objects.get(id=pk)
    form = SubPostModelForm()
    if request.method == 'POST':
        form=SubPostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-subpost')
    context = {'form':form}
    return render(request, 'post/subpost_form.html',context)
    '''
    if request.method == 'GET':
        
        return render(request, 'post/one_entry.html', context=context)
    elif request.method == 'POST':
        form = SubPostModelForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.user = request.user
            form.save()
            messages.success(request, f'Your subpost information has been created')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('subpost')
'''
class SubPostCreateView(CreateView):
    model = SubPost
    form_class = SubPostModelForm
    template_name='post/subpost_form.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url="/post-{post_id}"

@login_required
def updateSubpost(request,pk, id):
    subpost = SubPost.objects.get(id=id)
    
    if request.method == 'GET':
        form = SubPostModelForm(instance=subpost)
        context = {
            'heading': "Update the subpost Information",
            'form': form,
        }
        return render(request, 'post/subpost_form.html', context=context)
    
    if request.method == 'POST':
        form = SubPostModelForm(request.POST, instance=subpost)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your subpost information has been updated')
        else:
            messages.error(request, f'Something is wrong in your input')
        return redirect('post-detail', pk=pk)


@login_required
def deleteSubpost(request,pk, id):
    subpost = SubPost.objects.get(id=id).delete()
    messages.success(request, f'Your subpost information has been deleted')
    return redirect('post-detail', pk=pk)
