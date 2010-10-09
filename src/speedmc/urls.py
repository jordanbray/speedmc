from django.conf.urls.defaults import *
import speedmc.settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^stats/', include('speedmc.stats.urls')),
    (r'^map/', include('speedmc.map.urls')),
    (r'^$', 'basics.views.home'),
    (r'^login$', 'basics.views.login'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # DO NOT UNCOMMENT THIS IN A PRODUCTION ENVIRONMENT
    # IF THE NEXT TWO LINES ARE UNCOMMENTED IN ANYTHING OTHER THAN A DEV. ENVIRONMENT
    # COMMENT THEM OUT
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': speedmc.settings.PROJECT_DIR + '/static'}),
    (r'^credits/?$', 'basics.views.credits'),
    (r'^members/?$', 'basics.views.members'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
