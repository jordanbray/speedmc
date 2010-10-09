# Create your views here.
from django.http import HttpRequest, HttpResponse
from django.template import Context, loader
links = [
('location', 'name'),
('other location', 'other name'),
]
def home(request):
    t = loader.get_template('map/home.html')
#    c = Context({"links": links})
    c = Context({})
    return HttpResponse(t.render(c))