from django.conf.urls.defaults import *
import speedmc.settings

urlpatterns = patterns('',
    (r'^$', 'speedmc.map.views.home'),
)
