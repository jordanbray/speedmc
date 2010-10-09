# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader

def home(request):
    t = loader.get_template('home.html')
    c = Context({})
    return HttpResponse(t.render(c))

def credits(request):
    t = loader.get_template('credits.html')
    c = Context({})
    return HttpResponse(t.render(c))

def members(request):
    t = loader.get_template('members.html')
    c = Context({})
    return HttpResponse(t.render(c))

def login(request):
    t = loader.get_template('login.html')
    c = Context({})
    return HttpResponse(t.render(c))
