# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from message_management.models import Event

def add_message(request):
    return render_to_response('add_message.html', RequestContext(request))

def add_event(request):
    header = request.POST.get('msg_header')
    desc = request.POST.get('msg_desc')
    start = request.POST.get('msg_start')
    end = request.POST.get('msg_end')
    
    user = request.user.profile
    
    Event.objects.create_event(user,header,start,end,1)
    
    return redirect("/")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   