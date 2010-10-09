# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader
links = [
('/stats/', 'Users Logged On'),
('/stats/', 'Server Stats'),
('/stats/', 'Minecraft Stats'),
]
def home(request):
    t = loader.get_template('stats/home.html')
    c = Context({"links": links})
    return HttpResponse(t.render(c))