from datetime import timedelta, date, datetime
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf.urls import include
from message_management.models import Event, Msg
from user_management.models import UserFasadeInstance
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='/login')
def home(request):
    state = request.user.is_authenticated()
    user = UserFasadeInstance.objects.get_user_pyganizer_by_username(str(request.user.username))
    today = datetime.today()
    today_chuj = datetime(day=today.day, month=today.month, year=today.year, hour=0, minute=0)
    monday = today_chuj + timedelta(days=-today.weekday())
    sunday = monday + timedelta(days=7)
    print monday, sunday
    events_in_calendar = Event.objects.all(). \
        filter(start__gte=monday).filter(start__lte=sunday)
    events = []
    for event in events_in_calendar:
        events.append([event, event.start.weekday()])
    try:
        max_id = Event.objects.latest('id').id + 1
    except ObjectDoesNotExist:
        max_id = 1
    return render_to_response('home.html',
                              {'state': state, 'max_id': max_id, 'login': request.user.username, 'events': events},
                              RequestContext(request))

