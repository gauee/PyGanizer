from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf.urls import include

@login_required(login_url='/login')
def home(request):
    state = request.user.is_authenticated()
    return render_to_response('home.html', {'state':state,'login':request.user.username}, RequestContext(request))

