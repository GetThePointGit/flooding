from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import lizard_base.urls
import lizard_flooding.urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/', include(admin.site.urls)),
    (r'^flooding/', include(lizard_flooding.urls)),
    (r'', include(lizard_base.urls)),
    )


if settings.DEBUG:
    # Add this also to the projects that use this application
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )
