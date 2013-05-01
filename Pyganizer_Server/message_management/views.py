# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext

def add_message(request):
    return redirect("/")