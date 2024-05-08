from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Topic, Comment
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .form import createPost, createTopics
from django.contrib.auth.forms import UserCreationForm




# Create your views here.
def index(request):
    # gets all the fields from topic table
    topic = Topic.objects.all
    #for getting the search params
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    #for searching on the basis of topic name, post name,  username
    post = Post.objects.filter(Q(topic__topic__icontains=q) | Q(heading__icontains = q) | Q(desc__icontains=q) | Q(user__username__icontains=q) )
    post_count = post.count()
    return render(request, "post/home.html", {'post' : post, 'topic' : topic, 'post_count' : post_count})


def single(request, pk):
    #this id = pk gets the object that matches
    post = Post.objects.get(id=pk)
    comment_message = post.comment_set.all().order_by('-created')

    return render(request, "post/single.html", {'post' : post, 'comments' : comment_message})

# checks authentication so that only logged in can create 
@login_required(login_url = 'login')
def create(request):
    # imported the form
    form = createPost()
    # cheks if submited
    if request.method == 'POST':
        # fills the form with entered info
        form = createPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'post/createPost.html', {'form' : form})

@login_required(login_url = 'login')
def update(request, pk):
    
    post = Post.objects.get(id = pk)
    # so that u cant update if you aint the user that created
    if request.user != post.user:
        return HttpResponse("Unavailaable")
        # fills the form with selected post to update or edit
    form = createPost(instance = post)
    if request.method=='POST':
        form = createPost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'post/createPost.html', {'form':form})

@login_required(login_url = 'login')
def delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('home')
    return render(request, 'post/delete.html')

def loginPage(request):
    page='login'
    # u cant enter login page if already logged in
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            # u cant log in if not registered
            user = User.objects.get(username=username)
        except:

            messages.error(request, "User does not exist")
        # authentication stuff
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")
    return render(request, 'post/login_register.html', {'page' : page})


def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Something went error")
    return render(request, 'post/login_register.html', {'form' : form})


def createTopic(request):
    form = createTopics()
    if request.method == 'POST':
        form = createTopics(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    return render(request, 'post/createTopic.html', {'form' : form})