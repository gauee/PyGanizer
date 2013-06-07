from json import dumps
from django.http import HttpResponse


def sayhello(request):
    return HttpResponse(dumps({'message': 'Hello World'}))