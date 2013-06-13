from datetime import timedelta, datetime, date
from json import dumps, loads
from django.http import HttpResponse
from message_management.models import Event
from user_management.models import UserFasadeInstance

from django.core.exceptions import ObjectDoesNotExist


def sayhello(request):
    json_data = dumps({"HTTPRESPONSE": 1})
    print request.POST.keys()
    # json data is just a JSON string now.
    to_save_amount = int(request.POST.get("to_save_amount", False))
    to_del_amount = int(request.POST.get("to_delete_amount", False))
    #user = UserPyGanizer.objects.filter(userAuth=request.user)
    user = UserFasadeInstance.objects.get_user_pyganizer_by_username(str(request.user.username))
    today = date.today()
    monday = today + timedelta(days=-today.weekday())

    for i in range(to_save_amount):
        start = int(request.POST.get("to_save["+str(i)+"][start]").replace(":",""))
        stop = int(request.POST.get("to_save["+str(i)+"][stop]").replace(":",""))
        day = int(request.POST.get("to_save["+str(i)+"][day]"))

        #start_m = start[-2:]
        #start_h = start[:len(start_m)-1]
        #stop_m = stop[-2:]
        #stop_h = stop[:len(stop_m)-1]

        #start_m = int(start_m)
        #start_h = int(start_h)
        #stop_m = int(stop_m)
        #stop_h = int(stop_h)
        print "EEEELELELELELELEL"
        print start
        print stop
        start_h = start/100
        start_m = start - 100*start_h
        stop_h = stop/100
        stop_m = stop - 100*stop_h

        day_to_insert = datetime(day=monday.day, hour=0, minute=0, month=monday.month, year=monday.year)\
                        + timedelta(days=day)
        print "YOYOYOYOYOYOYOYOYO"
        print day_to_insert + timedelta(hours=start_h, minutes=start_m),
        print day_to_insert + timedelta(hours=stop_h, minutes=stop_m),
        try:
            event = Event.objects.all().get(id=int(request.POST.get("to_save["+str(i)+"][id]")))
            print "JEST JUZ TAKI EVENT!!!!!"
            print event
            event.start=day_to_insert + timedelta(hours=start_h+2, minutes=start_m)
            event.end=day_to_insert + timedelta(hours=stop_h+2, minutes=stop_m)
            print event.msgId.msgHeader
            event.msgId.msgHeader=request.POST.get("to_save["+str(i)+"][description]", False)
            print event
            event.save()
        except ObjectDoesNotExist:
            print "TWORZE NOWY OBIEKT"
            e = Event.objects.create_event(
                None,
                user,
                request.POST.get("to_save["+str(i)+"][description]", False),
                day_to_insert + timedelta(hours=start_h+2, minutes=start_m),
                day_to_insert + timedelta(hours=stop_h+2, minutes=stop_m),
                1
            )
            e.save()


        #return HttpResponse(dumps({'message': 'Hello World'}))
    for i in range(to_del_amount):
        try:
            print request.POST.get("to_delete["+str(i)+"][id]")
            event = Event.objects.all().get(id=int(request.POST.get("to_delete["+str(i)+"][id]")))
            event.delete()
        except ObjectDoesNotExist:
            return

    return HttpResponse("OK!")