# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
from message_management.models import Event, MsgFromFriend,StickyNote
from user_management.models import UserFasadeInstance

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


def send_msg_to_friend_form(request):
    friends = UserFasadeInstance.objects.get_user_friends(request.user)
    print(friends)
    return render_to_response('send_msg_to_friend.html', {'friends':friends},RequestContext(request))

def send_msg_to_friend(request):
    
    toUser = request.POST.get('toUser')
    toUser = UserFasadeInstance.objects.get_user_pyganizer_by_username(toUser)
    msg_header = request.POST.get('msg_header')
    msg_body = request.POST.get('msg_body')
    
    MsgFromFriend.objects.create_msg_to_friend(request.user.profile,toUser,msg_header,msg_body)
    
    return redirect ("/")

def show_my_messages(request):
    messages = MsgFromFriend.objects.get_all_messages(request.user)
    print(messages)
    return render_to_response('show_my_messages.html', {'messages':messages},RequestContext(request))
    
    
def add_sticky_note_form(request):
    return render_to_response('add_sticky_note.html',RequestContext(request))
    
def add_sticky_note(request):
    
    msgHeader = request.POST.get('msg_header')
    endTime = request.POST.get('endtime')
    category = request.POST.get('category')
    
    StickyNote.objects.create_sticky_note(request.user.profile,msgHeader,endTime,category)
    
    return redirect("/")
    
    
    
    
    
    
    
   