# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user_management.models import UserPyGanizerLabel, UserPyGanizer

def login_user(request):
    state = "Zaloguj się do aplikacji"
    
    if request.POST:
        if 'register' in request.POST:
            return redirect("/registration")
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                state = "Twoje konto jest nieaktywne, skontaktuj się z administratorem"
        else:
            state = "Login lub hasło jest niepoprawne"
            
    
    
    return render_to_response('login.html',{'state':state}, RequestContext(request))

def registration_user(request):
    state = "Zarejestruj się"
    if request.POST:
        if 'goToLogin' in request.POST:
            return redirect("/login")
        
        username = request.POST.get('username')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        password = request.POST.get('password')
        email = request.POST.get('email')
        desc =request.POST.get('desc')
        
        try:
            validLogin = User.objects.get(username = username)
            if validLogin:
                state = "Użytkownik o podanym loginie już istnieje"
                return render_to_response('registration.html',{'state':state},RequestContext(request))
        except User.DoesNotExist:
            user = User.objects.create_user(username, email, password)
            user.first_name = name
            user.last_name = surname
            user.save()
            userPyganizer = UserPyGanizer()
            userPyganizer.extraInfo = desc
            userPyganizer.userAuth = user
            userPyganizer.save()
            user = authenticate(username=username,password=password)
            login(request,user)
            context_info = "Witaj w aplikacji PyGanizer"
            return redirect('/')
        
    return render_to_response('registration.html',{'state':state},RequestContext(request))

def logout_user(request):
    logout(request)
    return redirect("/")
    
def users_all(request):
    users = UserPyGanizer.objects.all()
    label = list(UserPyGanizerLabel.objects.values_list('label', flat=True).order_by('orderId'))
    print(label)
    return render_to_response('users_all.html',{'users':users,'label':label},RequestContext(request))
    
    
def user_stats(request):
    user = request.user
    return render_to_response('user_stats.html',{'login':user.username,'name':user.first_name,'surname':user.last_name,'email':user.email,'creationDate':user.date_joined},RequestContext(request))


def insert_label(request):
    l = request.POST.get('label')
    n = request.POST.get('order')
    
    label = UserPyganizerLabel(label = l, orderId = n)
    label.save()
    return redirect("/")


def show_friends(request):
    user = request.user.profile    
    
    #print(user.friends.all())
    friends = user.friends.all()
    return render_to_response('show_friends.html',{'friends':friends},RequestContext(request))
    return redirect("/")


def add_friend(request):
    friends = list(request.user.profile.friends.all())
    friends.append(request.user.profile)
    users = UserPyGanizer.objects.exclude(userAuth__in=[o.userAuth for o in friends])
    
    return render_to_response('add_friend.html',{'users':users},RequestContext(request))
    #myFriends = Friends.objects.

def add_user_to_friend(request):
    choice = request.POST.get('friend','')
    if choice == '':
        return redirect("/add_friend")
    
    user = request.user.profile
    friendToAdd = UserPyGanizer.objects.get(id = choice)

    user.friends.add(friendToAdd)
    friendToAdd.friends.add(user)
    context_info = "Dodano do znajomych"
    
    return redirect("/show_friends",{'context_info':context_info})
        
