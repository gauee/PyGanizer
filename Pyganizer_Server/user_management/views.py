# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_user(request):
    state = "Please log in below...."
    username = 'admin'
    password = 'admin'
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                state = "Your account is not active, please contact the site"
        else:
            state = "Your username and/or password were incorrect."
            
    
    
    return render_to_response('login.html',{'state':state,'username':username,'password':password},RequestContext(request))

def registration_user(request):
    state = "Please registrate there"
    username = 'gauee'
    password = 'pass'
    if request.POST:
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.create_user(username, email, password)
        user.first_name = name
        user.last_name = surname
        user.save()
        
    return render_to_response('registration.html',{'state':state,'username':username,'password':password},RequestContext(request))

def logout_user(request):
    logout(request)
    return redirect("/")
    
def users_all(request):
    users = User.objects.all();
    return render_to_response('users_all.html',{'users':users},RequestContext(request))
    
    
def user_stats(request):
    user = request.user
    return render_to_response('user_stats.html',{'login':user.username,'name':user.first_name,'surname':user.last_name,'email':user.email,'creationDate':user.date_joined},RequestContext(request))
        