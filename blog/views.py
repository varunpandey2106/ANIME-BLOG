from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User




#posts = [
   # {
        #'author': 'Varun Pandey',
        #'title': 'Blog Post 1',
        #'content': 'First post content',
        #'date_posted': 'August 27, 2018'
    #},
    #{
    #    'author': 'Adith Narein T',
    #    'title': 'Blog Post 2',
    #    'content': 'Second post content',
    #    'date_posted': 'August 28, 2018'
    #}
#]

# Create your views here.

class PostListView(ListView):
    model=  Post #tells listview what model to query to create the list view
    template_name= 'blog/home.html' #<app>/<model>_<view_type>.html
    context_object_name= 'posts' #looping over the variable in the template
    ordering=["-date_posted"]
    paginate_by=2

class UserPostListView(ListView):
    model=  Post #tells listview what model to query to create the list view
    template_name= 'blog/user_post.html' #<app>/<model>_<view_type>.html
    context_object_name= 'posts' #looping over the variable in the template
    ordering=["-date_posted"]
    paginate_by=2

    def get_queryset(self): #when GET request is made, this method is used to retrieve User object. from kwargs dictionary
        user=get_object_or_404(User,username=self.kwargs.get('username')) #if user exists, we can capture it in user variable
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model=  Post #tells listview what model to query to create the list view

class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post #tells listview what model to query to create the list view
    fields=['title', 'content']

    def form_valid(self,form):
        form.instance.author= self.request.user #takes that instance and sets it to current logged in user
        return super().form_valid(form) #runs form valid method on parent class
        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post #tells listview what model to query to create the list view
    fields=['title', 'content' ]

    def form_valid(self,form):
        form.instance.author= self.request.user #takes that instance and sets it to current logged in user
        return super().form_valid(form) #runs form valid method on parent class
    
    def test_func(self): #decorator, returns true or false, returns 403
        post= self.get_object() #gets the post that we are currently trying to update
        if self.request.user==post.author:
            return True
        return False
    #return 403 if current user is not author of the post he is trying to update
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=  Post #tells listview what model to query to create the list view
    success_url='/blog/'
    def test_func(self): #decorator, returns true or false, returns 403
        post= self.get_object() #gets the post that we are currently trying to update
        if self.request.user==post.author:
            return True
        return False
    #return 403 if current user is not author of the post he is trying to delete

def home(request):
    content={"posts":Post.objects.all()}
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html', content)

#views always need to return HTTP response or exception

def about(request):
   # return HttpResponse('<h1>Blog About</h1>')
   return render(request, 'blog/about.html',{"title": "About"})





