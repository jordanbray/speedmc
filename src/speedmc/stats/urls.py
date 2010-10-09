from django.conf.urls.defaults import *
import speedmc.settings

urlpatterns = patterns('',
    (r'^$', 'speedmc.stats.views.home'),
)
